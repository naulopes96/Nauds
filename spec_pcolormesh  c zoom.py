from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data1 = pd.read_csv('specf0_190922freerun_1medida.csv',delimiter='\t')

freq = np.linspace (280e6,330e6, 461)
freq = freq/1e8
t = np.arange (1,1500,1)

#print(data1)

fig, (ax0) = plt.subplots(1,1)
im = ax0.pcolormesh(freq, t, data1, cmap='viridis')


axins = ax0.inset_axes([0.1, 0.5, 0.47, 0.47])
axins.pcolormesh(freq, t, data1, cmap='viridis')
#axins.imshow(im)
# sub region of the original image
x1, x2, y1, y2 = 3, 3.1, 1, 200
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
# axins.set_xticklabels([])
# axins.set_yticklabels([])

ax0.indicate_inset_zoom(axins, edgecolor="black")




fig.colorbar(im, ax=ax0, label = 'Amp (dB)')
plt.xlabel('freq (Hz)')
plt.ylabel('tempo (s)')
plt.title ('Espectograma $f_0$ sem travamento')
plt.tight_layout()
plt.show()