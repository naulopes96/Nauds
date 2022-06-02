# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:46:42 2022

@author: lluca
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importante usar delimitador
data = pd.read_csv('0L315.csv',delimiter=';')


# print (data.min())
#freq = data['Freq']
print (data)
# print (806e6)


# x = np.arange(0,3398,1)

# plt.plot(x,freq,linewidth=0.3, color='black')
# plt.xticks([0,600,1000,1500,2000,2500,3000],)
# plt.xlabel('Tempo (s)')
# plt.ylabel('Frequência (Hz)')
# # plt.title('  Free Running N9310A at 10 MHz')
# plt.show()
