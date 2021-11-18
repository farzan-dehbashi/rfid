import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('mean.csv')
df.plot.line(x='distance',y='average', grid=True, title = 'test', color=(1.0, 0.3, 0.1))#, linestyle='--', marker='.')
#y=['Tag 1 (Half length)','Tag 2 (Half length)']
#, yerr='std'
#plt.xticks(df['Distance (cm)'])
plt.ylim((-70,-45))
plt.grid(True)

plt.show()