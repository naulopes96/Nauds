# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:07:51 2022

@author: lluca
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data1 = pd.read_csv('fo_travado_315.csv',delimiter=';')

data1 = data1.transpose()
# agora cada coluna é um frame 


#criando array das freq e do tempo
ldata = len(data1[0])
freq = np.linspace (169e6,189e6,ldata)
t = np.arange (1,1501,1)


fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range (0,100):
    amp = []

    for j in range (0,len(data1[0])):
        
        amp.append(data1[i][j])

    ax.plot(freq,amp,t[i],s=2,c = amp)
plt.xlabel('freq')
plt.ylabel('Amp (dB)')
ax.set_zlabel('tempo (s)')

plt.show()
'''
t = np.arange (1,1501,1)
fig = go.Figure(data=[go.Surface(z=data1, x=freq, y=t)])
fig.update_layout(title='F_o', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
'''