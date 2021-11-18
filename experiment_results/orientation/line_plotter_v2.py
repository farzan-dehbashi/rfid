##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: Nov 2021
## Modified: Nov 2021
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

import matplotlib.pyplot as plt
import pylab as plb
import pandas as pd

#summery_directory
path = './polished_stats.csv'
df = pd.read_csv(path)
x_axis = range(1, 17, 1)
colors = ['black', 'purple',
    'red', 'blue', 'grey', 'crimson', 'orange', 'green', 'deeppink', 'crimson', 'teal','#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600', 'black', 'purple',
    'red', 'blue', 'grey', 'crimson', 'orange', 'green']

for i in range(0, 331, 30):
    plt.plot(x_axis, df[str(i)], '-gD', color=colors[(i//30)-1], linewidth=1.0, label= str(i))

plb.rcParams['font.size'] = 12
plt.grid()
x_ticks = range(1, 17, 2)
plt.xticks(x_ticks)
plt.yticks([-45, -55, -65, -75])
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel('RSS(dBm)')
plt.xlabel('Transmission line length(cm)')
plt.show()
