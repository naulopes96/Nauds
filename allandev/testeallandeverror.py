# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:56:23 2022

@author: lluca
"""


import numpy as np
import matplotlib.pyplot as plt
import allantools as at 


m=[]
y = open("freerunningWG1.txt","r") 

for i in range (0,30,1):
    
    m.append(float(y.readline()))
    m[i] = (m[i]-100000)/100000
    



x = np.arange(0,30,1)

(t2, ad, ade, adn) = at.oadev(m,rate=1.0,data_type='freq',taus = x )







plt.plot(t2,ad)
plt.errorbar(t2,ad,yerr=ade,errorevery = 100)
plt.xscale("log")
plt.yscale("log")
plt.xlabel (r'$\tau$(s)')
plt.ylabel('Allan deviation')
plt.title('Allan Deviation 33500B (100 KHz)')