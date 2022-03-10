# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:19:45 2022

@author: lluca
"""



import numpy as np
import matplotlib.pyplot as plt
import allantools as at 
#from matplotlib import style 



m=[]
y = open("FRN9310A.txt","r") 

for i in range (0,3999,1):
    
    m.append(float(y.readline()))



j=0
h=0

print (type(m))

# for i in range (0,3999,1):
#     if m[i] >= 1e7:
#         j = j + 1
#     elif m[i]>= 9999999:
#         h = h + 1
#     elif m[i]<9999994:
#         print (i)
# print (3999-(j+h))