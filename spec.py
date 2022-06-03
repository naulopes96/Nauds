# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:46:42 2022

@author: lluca
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

data = pd.read_csv('fo_travado_315.csv',delimiter=';')

data = data.transpose()
# agora cada coluna é um frame 


#criando array das freq e do tempo
ldata = len(data[0])
freq = np.linspace (169e6,189e6,ldata)

t = np.arange (1,1501,1)

#print (len(data), len (freq)) 
'''
fig1 = plt.scatter(freq,data[0])
plt.show()
'''
imax = []
idxmax = []
for i in range (0,len(data)):
    maxx = data[i].max()
    idx_imax = data[i].idxmax()
    
    imax.append(maxx)
    idxmax.append(idx_imax)    
    
    #print (type(idx_imax))


#pegando as possições (como int) dos maximos 
m =[]

for i in range (0,len(idxmax)):
    n =[]

    for x in idxmax[i]:
        if x.isdigit():
            n.append(x)
    
    m.append( ''.join(n))
#    print (m)

#print (m)
        
    
for i in range (0,len(m)):
    m[i]= int(m[i])

#quanto q  o pico andou durante o espectograma

fsum = 0.0

for i in range (0,len(m)):
    
    fsum = fsum + abs(freq[m[i+1]]- freq[m[i]])
    
    #print (i,fsum)


print (fsum)
