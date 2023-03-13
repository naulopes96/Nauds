# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:13:37 2023

@author: Naudson Lopes
"""
import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

nome_pasta = './100323'

arq_pasta = []

#arq_pasta = os.walk(nome_pasta)


for diretorio, subpastas, arquivos in os.walk(nome_pasta):
    
    for arquivo in arquivos:
        arq_pasta.append(os.path.join(arquivo))
for i in range(len(arq_pasta)):
    arq_pasta[i] = nome_pasta + '/' + arq_pasta[i]



#print (arq_pasta)

j=0
k=1

while j in range (len(arq_pasta)-16):

    # 1)      #################### extrair f_rep #####################
    
    #dados provinientes do analisador de espectro RF N9310A
    
    print (arq_pasta[j+1])
    print (arq_pasta[j])
    data2 = pd.read_csv(arq_pasta[j+1], delimiter=',', header = 17)
    
    #print (data2)
    dados2 = {'freq': data2['Trace1 X'], 'Amp': data2['Trace1 Y']}
    
    data_rf = pd.DataFrame(dados2)
    i_amp_frep = data_rf['Amp'].idxmax()
    frep = int(data_rf['freq'][i_amp_frep])
    
    
    print (frep)
    
    ########################################################
    
    # 2)           ############## limpar dados do osc ###############
    
    #leitura do arquivo csv, caso o arquivo venha do osc da Tektronix há um cabeçalho (cujo este programa ja elimina)
    
    data1= pd.read_csv(arq_pasta[j], delimiter=',', header = 20) 
    
           
    
    # 3)          ####### Escolha de numeros de canais utilizados pelo osc #######

    # 3.a) ############## dados em apenas 1 canal ##############

    # dados = {'tempo': data1['TIME']/10, 'Amp': data1['CH1']} # dados no canal 1
    # #dados = {'tempo': data1['TIME']/10, 'Amp': data1['CH2']} # dados no canal 2

                           ##########

    # 3.b) ############## dados em ambos canais ################

    dados = {'tempo': data1['TIME']/10, 'Amp1': data1['CH1'],'Amp2': data1['CH2']} 

    ######################################################

    data_osc = pd.DataFrame(dados) # salvando dados em um dataframe
    #data.to_csv('medida1_260micro_densidade_smedia(limpo).csv')


    # 4)                    ###### Plots #####

    # 4.a)  ############## plot com apenas 1 canal ################

    # fig,axs = plt.subplots(1,1,sharex=True)

    # axs.plot(data_osc['tempo'],data_osc['Amp2'], label = 'frep: ' + str(frep))
    # #plt.plot (data_osc['tempo'],data_osc['Amp1'], label = 'frep: ' + str(frep))
    # #plt.plot(data_osc['tempo'],data_osc['Amp'])
    # plt.xlabel('tempo (s)')
    # axs.set_ylabel('amplitude (u.a)')
    # axs.grid(True)

    # plt.legend()
    # plt.show()

    # 4.b) ############## plot para 2 canais ##########################

    fig,axs = plt.subplots(2,1,sharex=True)

    axs[0].plot(data_osc['tempo'],data_osc['Amp1'])
    axs[0].set_ylabel ('amplitude (u.a)')
    axs[0].grid(True)

    axs[1].plot(data_osc['tempo'],data_osc['Amp2'], label = 'frep: ' + str(frep))
    #plt.plot (data_osc['tempo'],data_osc['Amp1'], label = 'frep: ' + str(frep))
    #plt.plot(data_osc['tempo'],data_osc['Amp'])
    plt.xlabel('tempo (s)')
    axs[1].set_ylabel('amplitude (u.a)')
    axs[1].grid(True)
    
    fname = 'medida '+ str(k)
    plt.title(fname)
    plt.legend()
    
    plt.savefig(fname)
     
    data1 = []
    data2 = []
    k=+1
    j = j+2