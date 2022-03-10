# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:30:36 2022

@author: lluca
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importante usar delimitador
data = pd.read_csv('Frep_2travado(0803_tarde)_2.csv',delimiter=';',header=0,names=['Freq'])


# print (data.min())
freq = data['Freq']
print (freq[freq<10462238])
# print (806e6)


# x = np.arange(0,3398,1)

# plt.plot(x,freq,linewidth=0.3, color='black')
# plt.xticks([0,600,1000,1500,2000,2500,3000],)
# plt.xlabel('Tempo (s)')
# plt.ylabel('Frequência (Hz)')
# # plt.title('  Free Running N9310A at 10 MHz')
# plt.show()
