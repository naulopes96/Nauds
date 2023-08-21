import pyvisa
import time
from datetime import datetime
import pandas as pd

rm = pyvisa.ResourceManager()
list_inst = rm.list_resources()
print(list_inst[0])
inst = rm.open_resource('{}'.format(list_inst[0]))
N=5
freq = N*[0]
t=N*[0]
for i in range(N):
    inst.write('*IDN?')
    t[i] = datetime.now()
    t[i] = str(t[i])
    t[i] = t[i][11:]
    freq[i] = inst.read()

df = pd.DataFrame({'freq': freq ,'tempo': t})
print(df)