# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:31:34 2022

@author: lluca
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import allantools as at 
#from matplotlib import style 









data1 = pd.read_csv('frep_travado(0803_tarde).csv',delimiter=';',header=0,names=['Freq'])


# print (data['Freq'])
freq1 = data1['Freq']

m=[]


for i in range (0,2364):
    s = (freq1[i]-806e6)/806e6
    m.append(s)
    s=0


x = np.arange(0,2364,1)

(t2, ad, ade, adn) = at.oadev(m,rate=1,data_type='freq',taus = x )

###################################################################
n=[]

data2 = pd.read_csv('frep_rapido_30min.csv',delimiter=';',header=0,names=['Freq'])


# print (data['Freq'])
freq2 = data2['Freq']

n=[]


for i in range (0,2007):
    s = (freq2[i]-806e6)/806e6
    n.append(s)
    s=0

b = np.arange(0,2007,1)

(t3, ad3, ade3, adn3) = at.oadev(n,rate=1,data_type='freq',taus = b )


###################################################################
# p =[]
# q = open("10MHz1h1s_33500bwCsClk.txt","r") 

# for i in range (0,2383,1):
    
#     p.append(float(q.readline()))
    
#     p[i] = (p[i]-1e7)/1e7


# r = np.arange(0,2383,1)

# (t4, ad4, ade4, adn4) = at.oadev(p,rate=1,data_type='freq',taus = r )



####################################################################
p =[]

data3 = pd.read_csv('freptravado.csv',delimiter=';',header=0,names=['Freq'])

freq3 = data3['Freq']


for i in range (0,3292):
    s = (freq3[i]-806e6)/806e6
    p.append(s)
    s=0


r = np.arange(0,3292,1)

(t4, ad4, ade4, adn4) = at.oadev(p,rate=1,data_type='freq',taus = r )

####################################################################
fig, ax1 = plt.subplots(figsize=[6,6])






ax1.plot(t2,ad,linewidth=1,label = '$f_{rep}$ fast&slow lckd 08/03')
#ax.errorbar(t2,ad,yerr=ade,errorevery=70,ecolor='black')

ax1.plot(t3,ad3,linewidth=1,color = 'g', label = '$f_{rep}$ fast lckd 08/03')
# ax.errorbar(t2,ad,yerr=ade,errorevery=70,ecolor='black')


ax1.plot(t4,ad4,linewidth=1,label = '$f_{rep}$ fast&slow lckd 07/03', color ='purple')
# #ax.errorbar(t2,ad,yerr=ade,errorevery=70,ecolor='black')
#

plt.style.use('default')
plt.xscale("log")
plt.yscale("log")
plt.grid('true',which='both')
plt.xlabel (r'$\tau$(s)')
plt.ylabel('Allan deviation')
plt.legend()
plt.title('Allan Deviation $f_{rep}$ comparison') 
plt.show()