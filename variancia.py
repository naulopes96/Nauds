# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:19:29 2022

@author: LabDF
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import allantools as at 
import statistics as st
#from matplotlib import style 


#y = open("FRN9310A.txt","r") 

data = pd.read_csv('OADEV_OldCsClk10Mhz_1medida.txt',delimiter=';',names=['Freq'])

freq = data['Freq']
ldata =len(freq)
m=[]


for i in range (0,ldata):
    s = (freq[i]-838e6)/838e6
    m.append(s)
    s=0

var= (ldata-2)*[0]

for i in range(2,len(freq)):
     var[i-2]= st.variance(freq[:i])

var = var**(0.5)
x = np.arange (0,len(var),1)


plt.plot(x,var)
plt.style.use('default')
plt.xscale("log")
plt.yscale("log")
plt.grid('true',which='both')

plt.show()
