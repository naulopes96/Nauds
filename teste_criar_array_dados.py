# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 21:18:38 2022

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

matriz = [[],
          [],
          [[]]]

'''
matriz[0] = [1,11]
matriz[1] = [2,22]
matriz[2] = [[3,33],[1]]

'''
for i in range  (0,len(freq)):
    matriz[0].insert(i,freq[i])
    
for i in range  (0,len(t)):
    matriz[1].insert(i,t[i])
    

for i in range (0,1500):
    amp =[]
    for j in range (0,461):
        amp.append(data1[i][j])
    
    matriz[2].insert(i,amp)
    
    
#[0][i] = freqs;[1][j] = instantes; [2][i][j] = amp

print (matriz[0][0],matriz[1][0],matriz[2][0][0]) 

