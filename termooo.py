# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:02:37 2022

@author: lluca
"""
import pandas as pd 

data = pd.read_csv('br.txt', delimiter =' ', header= None, names = ['palavras'])

p = data.palavras

lp = len(p)


# #palavras com 5 letras
# s=[]

# for i in range (0,lp):
    
#     if len(p[i]) == 5:
#         s.append(p[i])    
#     else :
#         None 



# #meu chute e resultado
# g = input('Seu chute \n')

# r = input('Sequencia: v = verde,a = amarelo e c=cinza \n')

# attguess = []
# exguess = []
# nexguess = []
# for i in range (0,5):
#     if r[i] == 'v':
#         att = g[i]
#         attguess.insert(i,att)
#     elif r[i] == 'c':
#         attguess.insert(i,str(0))
#         nexguess.append(g[i])
#     elif r[i] == 'a':
#         attguess.insert(i,str(0))
#         exguess.append(g[i])
    
# s_attguess = ''.join(attguess)
# print (s_attguess,exguess,nexguess)
# #ate aqui meu codigo guarda a lista de todas as palavras com 5 letras
# #recebe input do chute e do resultado, analisa o resultado (para v,a,c)

teste = input('Nome \n')
l = teste.format('n')

print (l)