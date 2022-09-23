from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data1 = pd.read_csv('specf0_190922freerun_1medida.csv',delimiter='\t')
freq = np.linspace (280e6,330e6, 461)
t = np.arange (1,1500,1)

#print(data1)

fig, (ax0) = plt.subplots(1,1)
im = ax0.pcolormesh(freq, t, data1, cmap='viridis')
fig.colorbar(im, ax=ax0, label = 'Amp (dB)')
plt.xlabel('freq (Hz)')
plt.ylabel('tempo (s)')
plt.title ('Espectograma $f_0$ sem travamento')
plt.tight_layout()
plt.show()