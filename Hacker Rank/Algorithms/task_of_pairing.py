#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#

def taskOfPairing(freq):
    num_pairs = 0
    for i in range(len(freq)):
        if i == 0:
            while freq[0] > freq[1]:
                num_pairs += 1
                freq[0] -= 1
                next
            while (freq[0] <= freq[1]) and (freq[0] > 0):
                num_pairs += 1
                freq[0] -= 1
                freq[1] -= 1
                next
            if freq[0] == 0:
                next
        elif (i > 0) and (i < len(freq)):
            while freq[i - 1] > freq[i]:
                num_pairs += 1
                freq[i - 1] -= 1
            while (freq[i - 1] <= freq[i]) and (freq[i - 1] > 0):
                num_pairs += 1
                freq[i - 1] -= 1
                freq[i] -= 1
                next
            if freq[i - 1] == 0:
                next
        elif i == len(freq):
            while freq[i] > 1:
                num_pairs += 1
                freq[i] -= 1
            if freq[i] <= 1:
                break
    #print(num_pairs)
    return num_pairs
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    freq_count = int(input().strip())

    freq = []

    for _ in range(freq_count):
        freq_item = int(input().strip())
        freq.append(freq_item)

    result = taskOfPairing(freq)

    fptr.write(str(result) + '\n')

    fptr.close()