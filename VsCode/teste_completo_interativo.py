import pyvisa
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pathlib import Path
from playsound import playsound
from PIL import Image

def ler_canal (canal,n_pts_mode,n_pts):
    # a= str(n_pts_mode)
    # b= str(n_pts)
    inst1.write(':DIGitize [CHANnel{}:]'.format(canal))
    inst1.write(':WAVeform:SOURce CHANnel{}'.format(canal))
    inst1.write(':WAVeform:FORMat ASCii')

    ##### :WAVeform:POINts:MODE (NORMal | MAXimum | RAW); mais de 1000 pontos deve ter um :STOP
    ##### Se NORMal, POINts : {100 | 250 | 500 | 1000}
    ##### Se MAXimum ou RAW, POINts : {100 | 250 | 500 | 1000 | 2000 | 5000 | 10000 | 20000| 50000 
    #                                 | 100000 | 200000 | 500000 | 1000000 | 2000000| 4000000 | 8000000}

    #inst.write(':WAVeform:POINts:MODE NORMal')

    inst1.write(':WAVeform:POINts:MODE {}'.format(n_pts_mode))
    #inst.write(':WAVeform:POINts:MODE RAW')

    inst1.write(':WAVeform:POINts {}'.format(n_pts))
    inst1.write(':WAVeform:DATA?')

    y = inst1.read()
    y = y[10:]
    y= y.split(',')

    y = [float(i) for i in y]
    return y

rm = pyvisa.ResourceManager()
list_inst = rm.list_resources()

print('########## Programa FODA para resultados QUENTES ###############')
print('Osciloscópio 4 canais Agilent (DSO7104B): "USB0::0x0957::0x175D::MY50340840::INSTR" \n')
print('Osciloscópio 2 canais Agilent (DSOX2012A): "ainda nao sei rsrs" \n')
print('Contador de frequências (53132A) depende da porta do hub (checar hub). \n')

print('Lista de instrumentos \n',list_inst,'\n')
c1 = int(input('Endereço do Osciloscópio: '))
c2 = int(input('Endereço do Contador de frequencias: '))
c3 = int(input('Numero de pts no osciloscópio (100 | 250 | 500 | 1000 | 2000 | 5000 ):'))

#print(type(list_inst[0]))
print("'{}'".format(list_inst[c1]),'\n')
print("'{}'".format(list_inst[c2]),'\n')
# print('{}'.format(list_inst[choice2]),'\n')

inst1 = rm.open_resource('{}'.format(list_inst[c1]))
inst1.write(':STOP')

volt1 = ler_canal(1,'MAXimum',c3)
volt2 = ler_canal(2,'MAXimum',c3)
volt3 = ler_canal(3,'MAXimum',c3)
volt4 = ler_canal(4,'MAXimum',c3)

inst2 = rm.open_resource('{}'.format(list_inst[c2]))
inst2.write('*IDN?')
t_frep = datetime.now()
t_frep = str(t_frep)
t_frep = t_frep[11:]
freq = inst2.read()

# vetor tempo
inst1.write(':WAVeform:XORigin?')
x_0 = float(inst1.read())
inst1.write(':WAVeform:XINCrement?')
dx= float(inst1.read())
inst1.write(':RUN')

tf = x_0+len(volt1)*dx
t = np.arange(x_0,tf,dx)
t = [round(i,7) for i in t]
df = pd.DataFrame({'hr_medida':t_frep,'frep':freq,'tempo': t, 'channel1':volt1,'channel2':volt2,'channel3':volt3,'channel4':volt4})

###################### salvando o arquivo de maneira personalizada ##################

hr = datetime.now()
hr = str(hr)
#print(hr)
dia = hr[:10]
dia = dia.replace('-','_')
hr = hr[11:19]
hr = hr.replace(':','_')

pasta = rf'C:\Users\Marcio\Documents\TiS comb\Instrumentação\{dia}'

Path(pasta).mkdir(parents=True,exist_ok= True)

count = np.random.randint(0,2)
if count == 1:
    playsound('audios/ta virando um caberé aqui essa porra.mp3')
if count == 0:
    playsound('audios/vcs tem q tirar essa porra hj.mp3')

im = mpimg.imread('fundo.png')
imgplot = plt.imshow(im)
plt.show()

# trocar .csv por .npy pra mtos arquivos que nao precisa ver o conteudo

df.to_csv(rf'{pasta}\{hr}.csv',';')

