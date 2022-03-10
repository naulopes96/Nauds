# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:10:05 2022

@author: lluca
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import allantools as at 
#from matplotlib import style 


#y = open("FRN9310A.txt","r") 

data = pd.read_csv('Frep_2travado(0803_tarde)_2.csv',delimiter=';',header=0,names=['Freq'])


# print (data['Freq'])
freq = data['Freq']

m=[]


for i in range (0,3496):
    s = (freq[i]-806.4e6)/806.4e6
    m.append(s)
    s=0
    

# print (m[1000])

x = np.arange(0,3496,1)


(t2, ad, ade, adn) = at.oadev(m,rate=1,data_type='freq',taus = x )

#err = []
#for i in range (0,9253,1):
#    err[i] = ad[i]*1e-3/t2[i]




plt.plot(t2,ad,linewidth=1,color = 'k')
plt.errorbar(t2,ad,yerr=ade,errorevery=96,ecolor='blue')
plt.style.use('default')
plt.xscale("log")
plt.yscale("log")
plt.grid('true',which='both')
plt.xlabel (r'$\tau$(s)')
plt.ylabel('Allan deviation')
plt.title('Allan Deviation $f_{rep}$ fast&slow (08/03_2ª medida) gt= 1s') 
