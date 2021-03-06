# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:44:13 2021

@author: lluca
"""

import numpy as np
import random
from random import choice
import matplotlib.pyplot as plt
import time 

# 20x22 e t =10 000 => 7min30s
# 5x5 e t = 10 000 => 1min s/ loop da temp
# 10x10 e t = 10 000 => 2min
# 5x5, t= 1000 ,40 pts temp => 2min
# 10x10, t = 1000, 100 pts de temp => 16 min
# 10x10, t = 100, 100 pts de temp => 1min40s
# 10x10, t = 100, 200 pts de temp => 4min
# 10x10, t = 100, 500 pts de temp => 8min
# 20x20, t = 50,  100 pts de temp=> 7min
# 10x10, t = 1 000, 100 pts temp => 16 min


tsim1 = time.time()
N = 10
#no artigo enviado, em python a grade era 5x5

state = np.random.random((N,N))

for i in range (N):
    for j in range (N):
        if state[i][j] < 1:
            state[i][j] = 1
        else:
            state[i][j] = -1 
        




plt.imshow(state)
plt.show()


def calcenergia (state):

    i = 0
    j = 0
    istate = state
    
    comparar = np.arange (0,N,1)
    ene = 0
    
    for i in range (N):
            for j in range (N):
                
                ip = (i+1) 
                if ip in comparar:
                    cip= istate[i][j]*istate[ip][j]
                else:
                    cip = 0
                    
                ine = (i-1) 
                if ine in comparar:
                    cine = istate[i][j]*istate[ine][j]
                else:
                    cine = 0
                    
                jp = (j+1) 
                if jp in comparar:
                    cjp = istate[i][j]*istate[i][jp]
                else:
                    cjp = 0
                    
                jne = (j-1) 
                if jne in comparar:
                    cjne = istate[i][j]*istate[i][jne]
                else:
                    cjne = 0
                
                ene = ene + cip + cine + cjp + cjne
                
    '''    
    print (- ene)
    '''
    return (- ene)
    

def flip (state):
    state = state.copy() 
    istate = state
    flipx = random.randrange(0,N)
    flipy = random.randrange(0,N)
    
    
#    print (flipx,flipy)
    istate [flipx][flipy] = -1*istate [flipx][flipy] 
    
    return (istate)

T = 0.5
k=0
m_t = np.zeros(100)
e_t = np.zeros(100)
temp = np.zeros(100)
#for da temperatura a partir daqui
for k in range (100):
    state = state.copy()
#    state = np.random.random((N,N))
#
#    for i in range (N):
#        for j in range (N):
#            if state[i][j] >= 0.8:
#                state[i][j] = 1
#            else:
#                    state[i][j] = -1 
                    
   
    energia = 0
    
    t=100
    dt = 0
    
    net_spins = np.zeros(t)
    net_energia = np.zeros (t)
    #print (net_spins)
    
    for dt in range (t): 
        ene1 = calcenergia (state)
        energia = ene1
        fstate = flip (state)
    #print (state)
    #print (fstate)
    #
        ene2 = calcenergia (fstate)
        dE= ene2 - ene1
    
    #print(ene1+dE)
    #print (dE,w,h)
        
        if (dE>0):
            r = np.random.random()
            w = np.exp(-dE/T)
            if r <= w:
                state = fstate
                energia = energia + dE
    #            print('1')
            else:
                state = state
                energia = energia
    #            print ('2')
            
        elif dE <= 0:
            
            state = fstate
            energia = energia + dE
    #        print ('3')
            
    #    print(state)
        am = state.sum()
        
        net_spins[dt] = np.abs(am)
        net_energia[dt] = energia 
        
        dt = dt + 1
        
    temp[k]= T   
    m_t[k] = net_spins[-10:].mean()
    e_t[k] = net_energia[-10:].mean()
    
    T = T + 0.1
    
#temp = np.arange (.2,1,.02)
plt.plot (temp,m_t/N**2)
plt.xlabel ('~T')
plt.ylabel ('Magnetiza????o M??dia')
plt.show()

plt.plot (temp,e_t/100)
plt.xlabel ('~T')
plt.ylabel ('Energia M??dia')
plt.show()
#
#x = np.arange(1,t+1,1)
#plt.plot (x,net_spins/N**2)
#plt.xlabel ('Flips')
#plt.ylabel ('media de spins')
#plt.show()
#
#plt.plot (x,net_energia)
#plt.xlabel ('flips')
#plt.ylabel ('E/J')
#plt.show()
#
#
tsim2 = time.time()
plt.imshow(state)
plt.show()

print (tsim2-tsim1)
