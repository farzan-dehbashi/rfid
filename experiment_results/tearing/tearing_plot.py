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
import numpy as np
import math

df = pd.read_csv('stats.csv')

x_axis = [6,7,11,16]
colors = ['black', 'purple',
    'red', 'blue', 'grey', 'crimson', 'orange', 'green', 'deeppink', 'crimson', 'teal']
averages = np.array(df['compensated_average'])
averages[1] = -80

plt.plot([1,2,3,4], averages, '-gD', color='firebrick', linewidth=1.0, label= 'tearing')



plb.rcParams['font.size'] = 12
plt.grid()
plt.xticks([1,2,3,4],['Cutting \n point1', 'Cutting \n point2', 'Cutting \n point3', 'No cut'])
plt.yticks([-52,-56,-60,-65])
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel('RSS(dBm)')
plt.xlabel('Button pressed')
plt.show()
