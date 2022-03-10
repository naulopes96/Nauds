# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:09:52 2022

@author: lluca
"""

import numpy as np
import matplotlib.pyplot as plt
import allantools as at 
# import csv

#Lendo arquivo de duas colunas apenas com open, read e split
#split quebra as linhas do arquivo

m=[]
n=[]
file = open('teste.txt','r')

#file.read armazena todo o conteudo em data, mas split armazena cada linha em 
#uma entrada de 'data'

data = (file.read()).split()

    
N = len (data)

for i in range (0,N):
    if (i % 2) != 0:
        m.append(data[i])
    elif i%2 == 0 :
        n.append(data[i])

plt.plot(n,m)
plt.xticks([200*1e6])
plt.yscale('log')

file.close()


