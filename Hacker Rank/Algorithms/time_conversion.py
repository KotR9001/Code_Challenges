#!/bin/python3

import os
import sys
import fnmatch

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #Split the Time Into Hours, Minutes, & Seconds
    time_list = s.split(':')
    #print(time_list)
    #print(int(time_list[0]))
    #Check if Hours is 12 & If Time is AM or PM
    #Found Method for Pattern Comparison at https://stackoverflow.com/questions/41969134/wildcard-matching-in-python
    if time_list[0] == '12' and fnmatch.fnmatch(time_list[2], '*AM'):
        time_list[0] == '00'
    elif time_list[0] != '12' and fnmatch.fnmatch(time_list[2], '*PM'):
        time_list[0] = str(int(time_list[0]) + 12)
        print(time_list[0])
    
    #Rejoin the List
    military_time = ":".join(time_list)
    #print(military_time)
    
    #Create List of All Characters in Time Stamp
    time = list(military_time)
    #Delete the Last Two Characters
    del time[-1]
    del time[-1]
    #Recreate the Military Time
    military_time = "".join(time)
    #print(military_time)
    return military_time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()