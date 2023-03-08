############ Plot Osciloscopio ##############

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data1= pd.read_csv('medida1_260micro_densidade_smedia.csv', delimiter=',', header = 20)

dados = {'tempo': data1['TIME'], 'Amp': data1['CH2']}

data = pd.DataFrame(dados)
# plt.plot (data1['TIME'],data1['CH2'])
# plt.grid('on')
# plt.show()
data.to_csv('medida1_260micro_densidade_smedia(limpo).csv')
print (data)