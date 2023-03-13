############ plot Osciloscopio + f_rep ##############
# falta otimizar pra ler todos os arquivos da pasta, neste formato tem que colocar 1 a 1

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# 1)      #################### extrair f_rep #####################

#dados provinientes do analisador de espectro RF N9310A

data2 = pd.read_csv('/EIT_100323\\medida9_frep.CSV', delimiter=',', header = 17)

#print (data2)
dados2 = {'freq': data2['Trace1 X'], 'Amp': data2['Trace1 Y']}

data_rf = pd.DataFrame(dados2)
i_amp_frep = data_rf['Amp'].idxmax()
frep = int(data_rf['freq'][i_amp_frep])

# print (frep)
########################################################

# 2)           ############## limpar dados do osc ###############

#leitura do arquivo csv, caso o arquivo venha do osc da Tektronix há um cabeçalho (cujo este programa ja elimina)

data1= pd.read_csv('/EIT_100323\\medida9_EIT_media4pts.CSV', delimiter=',', header = 20) 

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

fig,axs = plt.subplots(1,1,sharex=True)

axs.plot(data_osc['tempo'],data_osc['Amp2'], label = 'frep: ' + str(frep))
#plt.plot (data_osc['tempo'],data_osc['Amp1'], label = 'frep: ' + str(frep))
#plt.plot(data_osc['tempo'],data_osc['Amp'])
plt.xlabel('tempo (s)')
axs.set_ylabel('amplitude (u.a)')
axs.grid(True)

plt.legend()
plt.show()

# 4.b) ############## plot para 2 canais ##########################

# fig,axs = plt.subplots(2,1,sharex=True)

# axs[0].plot(data_osc['tempo'],data_osc['Amp1'])
# axs[0].set_ylabel ('amplitude (u.a)')
# axs[0].grid(True)

# axs[1].plot(data_osc['tempo'],data_osc['Amp2'], label = 'frep: ' + str(frep))
# #plt.plot (data_osc['tempo'],data_osc['Amp1'], label = 'frep: ' + str(frep))
# #plt.plot(data_osc['tempo'],data_osc['Amp'])
# plt.xlabel('tempo (s)')
# axs[1].set_ylabel('amplitude (u.a)')
# axs[1].grid(True)

# plt.legend()
# plt.show()