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
def Average(lst):
    return sum(lst) / len(lst)

if __name__ == '__main__':
    file_names = ['stats_1', 'stats_2','stats_3','stats_4','stats_5','stats_10','stats_20','stats_30','stats_40','stats_50','stats_100',]
    averages_vs_nsamples = [] # index 0 => 1 sample, index 1 => 2samples ... index 10 => 100 samples
    for file_name in file_names:
        df = pd.read_csv(f'./{file_name}.csv')
        col_names = ['average 1m', 'average 2m', 'average 3m', 'average 4m', 'average 5m', 'average 6m', 'average 7m', 'average 8m']
        #print(df.head(5))
        range_averages = [] # index 0 => 1m, index 1 => 2m, ...,index 7 => 8m
        for col_name in col_names:
            if col_name in df.columns:
                col_average = df[col_name].describe().loc['mean']
                range_averages.append(col_average)
                #print(f'{col_name} av= {col_average}')

            else:
                print(f'{col_name} does not exist in {file_name}')

        averages_vs_nsamples.append(Average(range_averages))

    #print(averages_vs_nsamples)
    errors = []
    for average in averages_vs_nsamples:
        av_error = average - averages_vs_nsamples[10]
        errors.append(av_error)
    print(errors)