# Author: Farzan Dehbashi
# Date: 2021/06/02
# Last modified: 2021/06/02
# Description: simple read from sllurp and R420

from sllurp.reader import R420_EU
import pandas as pd
import sys
import argparse
import time
import os

parser = argparse.ArgumentParser(description='Configuration for the reader')
parser.add_argument('-d', '--duration',type=float, metavar='', required=False, help='duration of the total run of the program in seconds')
parser.add_argument('-o', '--out', type=str, metavar='', required=True, help='output file name')
args = parser.parse_args()



#### arguments
ip = '169.254.1.1'
freq = '913.75'
duration = float(args.duration)
out = args.out

reader = R420_EU(ip)


#ideas to improve the rate:
    #add to csv every second or ...

tags = []
counter = 1 # every 10 run of inventory, it adds the read tags into the csv

#start_time = time.time()

#os.remove(str(out)+'.csv')

#df = pd.DataFrame({ 'EPCValue':'Dummy','TimeStamp':'Dummy','RunNum':'0','Antenna':'0','Power':32.5,'Reader':'0'})
#"EPCValue", "TimeStamp", "RunNum", "RSSI", "Reader", "Frequency", "Power", "Antenna"
#df.to_csv(str(out)+'.csv', mode= 'w', header=True, index=False)

first_read_flag = True

while True:
    ##### reads the tags
    tags = reader.detectTags(powerDBm=32.5, freqMHz=913.75, duration=0.05)

    for tag in tags:# stores the epc names of the chips
        if 'EPCData' in tag.keys() :
            EPCValue = tag['EPCData']['EPC']
        else:
            EPCValue = tag['EPC-96']
        if first_read_flag == True:
            first_read_flag = False
            #reads and saves the first line to with the column names:
            df = pd.DataFrame({'EPCValue': [EPCValue], 'TimeStamp': [tag['FirstSeenTimestampUTC']], 'RSSI': [tag['RSSI']],
                           'Frequency': [tag['ChannelIndex']], 'RunNum': '0', 'Antenna': '0', 'Power': 32.5,
                           'Reader': '0'})
            df.reindex()
            df.to_csv(str(out) + '.csv', mode='a', header=True, index=False)

        #adds the tags data into the data frame
        c = 1
        while c < tag['TagSeenCount']:
            c = c + 1
            df = pd.DataFrame({'EPCValue': [EPCValue], 'TimeStamp': [tag['FirstSeenTimestampUTC']], 'RSSI': [tag['RSSI']], 'Frequency': [tag['ChannelIndex']], 'RunNum':'0','Antenna':'0','Power':32.5,'Reader':'0'})

            df.reindex()
            df.to_csv(str(out)+'.csv', mode= 'a', header=False, index=False)


   # if time.time() - start_time > duration:
   #      break
