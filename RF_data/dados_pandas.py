# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:08:18 2022

@author: lluca
"""
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

#importante usar delimitador
data = pd.read_csv('FRPLCK.csv',delimiter=';',header=0)



t = np.arange(1,462,1)


#pontos medios de sinal do pico
mean=[]



for j in range (0,461):
    m=[]
    linha = data.loc[j]
    # print (linha)
    
    maxl = linha.max()
    maxlidx = int (linha.idxmax()) -1
    
    # print (maxl,maxlidx)
    
    for i in range (maxlidx-1,maxlidx + 2):
        m.append(linha[i])
    
    # print (np.mean(m))
    mean.append((np.mean(m)))
    # print (np.mean(m))
    
plt.scatter(mean,t)
plt.show()






















#qnd nossas colunas tem nome, basta chama-las pelo nome file ['nome_coluna']
# print (data['b'])

#se as colunas não tem nome/queremos rescrever o nome das colunas(no caso header=0 p/ reescrever)
# data = pd.read_csv('teste.csv',delimiter=';',header=0,names=['sinal','freq'])

# py.init_notebook_mode(connected=True)

# trace = go.Scatter(x=data['Sinal'],y=data['Freq'],mode = 'markers')


# g = [trace]

# py.iplot(g)