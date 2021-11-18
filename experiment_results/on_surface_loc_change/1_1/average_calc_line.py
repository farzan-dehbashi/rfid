import numpy as np
import pandas as pd
import os


file_names = np.arange(start=0, stop=16+1, step=1)
chip_name = '0x000000000000'

d = { 'average': []}
mean_df = pd.DataFrame(data=d)

for file_name in file_names: #file name is just a int
    if os.path.isfile('TH_'+str(file_name)+'.csv'):
        df = pd.read_csv('TH_'+str(file_name)+'.csv', names=["EPCValue", "TimeStamp", "RunNum", "RSSI", "Reader", "Frequency", "Power", "Antenna"])

        filt = (df['EPCValue'] == chip_name)
        filtered_df = df.loc[filt]

        RSSIs = filtered_df['RSSI']
        RSSIs = pd.to_numeric(RSSIs)
        mean_df.at[file_name, 'average'] = RSSIs.describe().loc['mean']
    #mean_df.at[file_name, 'std'] = RSSIs.describe().loc['std']
    #mean_df.at[file_name, 'count'] = RSSIs.describe().loc['count']

mean_df.to_csv('mean.csv')

