##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

import matplotlib.pyplot as plt
import pylab as plb
import numpy as np


average_err_vs_n_samples = np.array([0.10532081787305714, 0.07734462739686876, 0.0585946273968716, 0.046245726297968304, 0.02825007611481567, 0.022800213477452758, 0.01730799736023414, 0.013224086705676541])

# index ['stats_1', 'stats_2','stats_3','stats_10','stats_20','stats_30','stats_40','stats_50','stats_100',] stats_n_samples

plb.rcParams['font.size'] = 12
#xtics = np.array([1,2,3,10,20,30,40,50,100])
#xtics = xtics * 0.05 #second delay
x_tics = np.array([0.05, 0.1,  0.15, 0.5,  1.,   1.5,  2.,   2.5 ])*1000 #mseconds
plt.plot(x_tics,average_err_vs_n_samples, '-gD', color='firebrick', linewidth=3.0)
plt.grid()
#plt.legend()
plt.xticks(np.array([0.05, 0.5,  1.,   1.5,  2.,   2.5 ])*1000)
plt.yticks(np.array(range(0, 12, 2))/ 100)
plt.ylabel('Average error(dBm)')
plt.xlabel('Sampling delay(mS)')
plt.show()