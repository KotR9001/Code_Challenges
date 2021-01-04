#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_list = []
    color_count_list = []
    for color in ar:
        #Append Count to Unique Color List if First Instance of Color
        if color not in color_list:
            color_list.append(color)
            #Divide the Count by Two and Round Down to the Nearest Integer
            color_count_list.append(math.floor(ar.count(color)/2))
        #Otherwise Delete the Character from the Array
        else:
            del color
    matching_pairs = sum(color_count_list)
    #print(matching_pairs)
    return matching_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()