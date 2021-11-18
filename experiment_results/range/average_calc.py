##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: Nov 8th 2021
## Email: farzan.dehbashi95@gmail.com
## Status: developed
##################################################

import os
import pandas as pd

# Read all files in a folder and send back the average df

def read_csv_calc_summery(folder_name, file_name, mean_df, first_n_elements):

    df = pd.read_csv(f'./{folder_name}/TH_{file_name}.csv',
        names=["EPCValue", "TimeStamp", "RunNum", "RSSI", "Reader", "Frequency", "Power", "Antenna"])
    filt = (df['EPCValue'] == chip_name)
    filtered_df = df.loc[filt]
    filtered_df = filtered_df.head(first_n_elements)

    RSSIs = filtered_df['RSSI']
    RSSIs = pd.to_numeric(RSSIs)
    mean_df.at[file_name, f'average {folder_name}'] = RSSIs.describe().loc['mean']
    mean_df.at[file_name, f'std {folder_name}'] = RSSIs.describe().loc[
        'std']
    mean_df.at[file_name, f'count {folder_name}'] = RSSIs.describe().loc['count']
    return mean_df

# Read all folders

def folder_stats_calculator(folder_name, csv_names, mean_df, first_n_elements):

    for csv_name in csv_names:
        if os.path.isfile(f'./{folder_name}/TH_{csv_name}.csv'):
            mean_df = read_csv_calc_summery(folder_name, csv_name, mean_df, first_n_elements)

        else:
            print(f'./{folder_name}/TH_{csv_name}.csv does not exist')
    return mean_df

# Main

def main(mean_df):
    first_n_rows = [1,2,3,4,5,10,20,30,40,50,100]
    for first_n_row in first_n_rows:
        for folder_name in folder_names:
            if os.path.isdir(f'./{folder_name}/'):
                trial_df = folder_stats_calculator(folder_name, csv_names, mean_df, first_n_row) #first n


            else:
                print(f'Folder name {folder_name} does not exit')
        trial_df.to_csv(f'./err_first_n_rows/stats_{first_n_row}.csv')

if __name__ == '__main__':
    global chip_name
    global folder_names
    global csv_names
    global mean_df
    d = {'average': []}
    mean_df = pd.DataFrame(data=d)

    ### change these parameters
    folder_names = range(1, 16+1, 1)
    folder_names = ['1m','2m','3m','4m','5m','6m','7m','8m' ]
    csv_names = range(0, 16+1, 1)
    chip_name = '0xf91975000000'
    ############################

    main(mean_df)
