# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:24:23 2022

@author: Naudson Lopes
"""
import numpy as np
import matplotlib.pyplot as plt
import allantools as at 

m=[]
y = open("FRN9310A.txt","r") 

for i in range (0,3999,1):
    
    m.append(y.readline())
    
x = np.arange(0,3999,1)







#
#x2 = [300]*2
#y2 = [100000.085,100000.115]
#x3 = [600,600]




'''
plt.plot(x2,y2, c = 'gray')
plt.plot(x3,y2, c = 'gray')
'''

plt.plot(x,m) 

'''plt.ylim(100000.050,100000.130)'''


# plt.xticks([0,300,600,900])
plt.title('Free Running HP33120A (10MHz)')
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')


y.close()  




