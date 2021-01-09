#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    #Convert path into a List
    path_list = list(path)
    #print(f"The path list is: {path_list}")

    #Initialize Elevation & Number of Valleys Traversed
    elevation = 0
    num_valleys = 0
    step = 0

    #Loop Through path_list
    while step < len(path_list):
        #print(f"The step number is: {step}")
        #Increment or Decrement the Elevation
        if path_list[step] == 'U':
            elevation += 1
            #print(f"The elevation is: {elevation}")
        elif path_list[step] == 'D':
            elevation -= 1
            #print(f"The elevation is: {elevation}")

        #Keep Track of Number of Steps to Skip
        skip_steps = 0
        #If Elevation is Negative, Track Until it Reaches Sea Level
        if elevation < 0:
            for step1 in range(step+1, len(path_list)):
                #print(f"The step1 is: {step1}")
                #Increment or Decrement the Elevation
                if path_list[step1] == 'U':
                    skip_steps += 1
                    elevation += 1
                    #print(f"The elevation is: {elevation}")
                elif path_list[step1] == 'D':
                    skip_steps += 1
                    elevation -= 1
                    #print(f"The elevation is: {elevation}")
                if elevation >= 0:
                    num_valleys += 1
                    #print(f"The number of valleys traversed is: {num_valleys}")
                    #print(f"The step is: {step}")
                    break
        #print(f"Number of steps skipped is: {skip_steps}")
        if skip_steps == 0:
            step += 1
        elif skip_steps != 0:
            step += skip_steps + 1
            #print(f"The Step number is: {step}")

    #print(num_valleys)
    return num_valleys
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()