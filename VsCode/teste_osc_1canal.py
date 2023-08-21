import pyvisa
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


rm = pyvisa.ResourceManager()
list_inst = rm.list_resources()
print(list_inst)
inst = rm.open_resource('USB0::0x0957::0x175D::MY50340840::INSTR')
inst.write(':DIGitize [CHANnel1:]')
inst.write(':WAVeform:SOURce CHANnel1')
inst.write(':WAVeform:FORMat ASCii')

##### :WAVeform:POINts:MODE (NORMal | MAXimum | RAW)
##### Se NORMal, POINts : {100 | 250 | 500 | 1000}
##### Se MAXimum ou RAW, POINts : {100 | 250 | 500 | 1000 | 2000 | 5000 | 10000 | 20000| 50000 
#                                 | 100000 | 200000 | 500000 | 1000000 | 2000000| 4000000 | 8000000}

#inst.write(':WAVeform:POINts:MODE NORMal')
inst.write(':STOP')
inst.write(':WAVeform:POINts:MODE MAXimum')
#inst.write(':WAVeform:POINts:MODE RAW')

inst.write(':WAVeform:POINts 2000')
inst.write(':WAVeform:DATA?')

y = inst.read()
y = y[10:]
y= y.split(',')

y = [float(i) for i in y]

inst.write(':WAVeform:XORigin?')
x_0 = float(inst.read())
inst.write(':WAVeform:XINCrement?')
dx= float(inst.read())
inst.write(':RUN')

tf = x_0+len(y)*dx
t = np.arange(x_0,tf,dx)
t = [round(i,7) for i in t]
df = pd.DataFrame({'cha1': y ,'tempo': t})

hr = datetime.now()
hr = str(hr)
hr = hr[11:19]
hr = hr.replace(':','_')

file_name = 'C:\\Users\\Marcio\\Documents\\TiS comb\\Instrumentação\\' + hr + '.csv'

print (hr)

df.to_csv(file_name,';')

# print (dx,'\n')
# print(len(y),len(t),'\n')
# print(t[0],t[len(t)-1],tf)

# plt.plot(df['tempo'],df['cha1'])
# plt.grid('on')
# plt.show()
