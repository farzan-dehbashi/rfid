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
def read_csv_calc_summery(path):

def folder_stats_calculator(path, csv_names):
    for csv_name in csv_names:
        if os.path.isfile(f'./{path}/TH_{csv_name}.csv'):
            trial_summery_df = read_csv_calc_summery(f'./{path}/TH_{csv_name}.csv')
        else:
            print(f'./{path}/TH_{csv_name}.csv does not exist')
    return 0
# Main

def main():
    folder_range = range(1, 16+1, 1)
    cutting_range = range(0, 360+1, 30)
    for folder_name in folder_range:
        if os.path.isdir(f'./{folder_name}/'):
            trial_df = folder_stats_calculator(folder_name, cutting_range)
        else:
            print(f'Folder name {folder_name} does not exit')

if __name__ == '__main__':
    main()