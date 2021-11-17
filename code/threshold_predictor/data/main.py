import pandas as pd
from sklearn.datasets import load_boston
from optbinning import ContinuousOptimalBinning
import numpy as np
import pandas as pd
import os
import math

# Read csv files

def read_data(folder_name): # Outputs a list of all RSSi of a folder appended on top of each other
    file_names = np.arange(start=1, stop=16 + 1, step=1)
    chip_name = '0xf91975000000'
    appended_RSSIs = []
    d = {'average': []}
    mean_df = pd.DataFrame(data=d)

    for file_name in file_names:  # file name is just a int
        if os.path.isfile(f'./{folder_name}/TH_{file_name}.csv'):
            df = pd.read_csv(f'./{folder_name}/TH_' + str(file_name) + '.csv',
                             names=["EPCValue", "TimeStamp", "RunNum", "RSSI", "Reader", "Frequency", "Power", "Antenna"])
            filt = (df['EPCValue'] == chip_name)
            filtered_df = df.loc[filt]
            filtered_df = filtered_df.head(35)
            RSSIs = filtered_df['RSSI']
            RSSIs = RSSIs.tolist()
            print(file_name)
            print(RSSIs)
            print(len(RSSIs))
            appended_RSSIs = appended_RSSIs + [float(x) for x in RSSIs]

        else:
            print(f'file {folder_name}/{file_name} does not exist')

    #clean list
    # for element in appended_RSSIs:
    #     while appended_RSSIs.count(element) > 35:
    #         appended_RSSIs.remove(element)
    appended_RSSIs = np.sort(appended_RSSIs)
    return np.array(appended_RSSIs)

# Optimize number of bins

def optimize_bins(x, y, n_bins):
    optb = ContinuousOptimalBinning(dtype="numerical", min_n_bins = n_bins, max_n_bins= n_bins, min_mean_diff=3)
    optb.fit(x[:350], y[:350])

    print(optb.status)

    binning_table = optb.binning_table
    bin_table = binning_table.build()
    bin_table.to_csv(f'bin_table{n_bins}.csv')

    binning_table.plot(style="actual")
    print(binning_table.analysis())
# Main function

def main():
    x = read_data('1m') # Read data from data folder and append all RSS values and form a single df
    # x2 = read_data('2m')
    # x = list(x1) + list(x2)
    x = [item -1 for item in x]
    y = read_data('2m')
    #for n_bin in range(1, 9, 1):
    #    print(n_bin)
    optimize_bins(x,y, 3
    )

# Main

if __name__ == '__main__':
    main()


