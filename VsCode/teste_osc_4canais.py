import pyvisa
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def ler_canal (canal,n_pts_mode,n_pts):
    # a= str(n_pts_mode)
    # b= str(n_pts)
    inst.write(':DIGitize [CHANnel{}:]'.format(canal))
    inst.write(':WAVeform:SOURce CHANnel{}'.format(canal))
    inst.write(':WAVeform:FORMat ASCii')

    ##### :WAVeform:POINts:MODE (NORMal | MAXimum | RAW); mais de 1000 pontos deve ter um :STOP
    ##### Se NORMal, POINts : {100 | 250 | 500 | 1000}
    ##### Se MAXimum ou RAW, POINts : {100 | 250 | 500 | 1000 | 2000 | 5000 | 10000 | 20000| 50000 
    #                                 | 100000 | 200000 | 500000 | 1000000 | 2000000| 4000000 | 8000000}

    #inst.write(':WAVeform:POINts:MODE NORMal')

    inst.write(':WAVeform:POINts:MODE {}'.format(n_pts_mode))
    #inst.write(':WAVeform:POINts:MODE RAW')

    inst.write(':WAVeform:POINts {}'.format(n_pts))
    inst.write(':WAVeform:DATA?')

    y = inst.read()
    y = y[10:]
    y= y.split(',')

    y = [float(i) for i in y]
    return y

rm = pyvisa.ResourceManager()
list_inst = rm.list_resources()
print(list_inst)
inst = rm.open_resource('USB0::0x0957::0x175D::MY50340840::INSTR')

################ pegando dados dos canais ###################################

inst.write(':STOP')

volt1 = ler_canal(1,'MAXimum',2000)
volt2 = ler_canal(2,'MAXimum',2000)
volt3 = ler_canal(3,'MAXimum',2000)
volt4 = ler_canal(4,'MAXimum',2000)

# vetor tempo
inst.write(':WAVeform:XORigin?')
x_0 = float(inst.read())
inst.write(':WAVeform:XINCrement?')
dx= float(inst.read())
inst.write(':RUN')


tf = x_0+len(volt1)*dx
t = np.arange(x_0,tf,dx)
t = [round(i,7) for i in t]

df = pd.DataFrame({'tempo': t, 'channel1':volt1,'channel2':volt2,'channel3':volt3,'channel4':volt4})
#####################################################################################
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

#print (hr)

# trocar .csv por .npy pra mtos arquivos que nao precisa ver o conteudo

df.to_csv(rf'{pasta}\{hr}.csv',';')
#####################################################################################

# print (dx,'\n')
# print(len(y),len(t),'\n')
# print(t[0],t[len(t)-1],tf)

# plt.plot(df['tempo'],df['channel1'],c='yellow')
# plt.plot(df['tempo'],df['channel2'],c= 'green')
# plt.plot(df['tempo'],df['channel3'],c= 'blue')
# plt.grid('on')
# plt.show()
