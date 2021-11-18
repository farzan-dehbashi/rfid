##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################
import os
import pandas as pd

if __name__ == '__main__':
    file_names = ['stats_1', 'stats_2','stats_3','stats_4','stats_5','stats_10','stats_20','stats_30','stats_40','stats_50','stats_100',]
    for file_name in file_names:
        df = pd.read_csv(f'./{file_name}.csv')
        col_names = ['average 1m', 'average 2m', 'average 3m', 'average 4m', 'average 5m', 'average 6m', 'average 7m', 'average 8m']
        print(df.head(5))
        for col_name in col_names:
            if col_name in df.columns:
                col_average = df[col_name].describe().loc['mean']
                print(f'{col_name} av= {col_average}')
            else:
                print(f'{col_name} does not exist in {file_name}')
