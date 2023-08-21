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
print(list_inst)
inst1 = rm.open_resource('USB0::0x0957::0x175D::MY50340840::INSTR')

################ pegando dados dos canais ###################################

inst1.write(':STOP')

volt1 = ler_canal(1,'MAXimum',2000)
volt2 = ler_canal(2,'MAXimum',2000)

#medida do contador de freq
inst2 = rm.open_resource('ASRL7::INSTR')

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

df = pd.DataFrame({'hr_medida':t_frep,'frep':freq,'tempo': t, 'channel1':volt1,'channel2':volt2})
#####################################################################################
###################### salvando o arquivo de maneira personalizada ##################

hr = datetime.now()
hr = str(hr)
#print(hr)
dia = hr[:10]
dia = dia.replace('-','_')
hr = hr[11:19]
hr = hr.replace(':','_')

pasta = rf'C:\Users\Marcio\Documents\TiS comb\Instrumentação\{dia}' #criar nome da pasta

Path(pasta).mkdir(parents=True,exist_ok= True) #criar pasta

# trocar .csv por .npy pra mtos arquivos que nao precisa ver o conteudo

df.to_csv(rf'{pasta}\{hr}.csv',';')