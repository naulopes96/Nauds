# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:51:13 2022

@author: lluca
"""

import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0,10,11) 
t2 = np.linspace(0,20,21) 

v1 = 22.2 + 0*t
v2 = np.zeros(21)
for i in range (0,20,1):
    
    if  t2[i] < 10:
        v2[i] = 0
    else:
        v2[i] = 22.2 + t2[i]
    
#print (t2)
#print (v2)
#plt.plot(t,v1)
plt.plot(t2,v2)