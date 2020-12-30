#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    #Create Empty Lists for Storing Values
    positive_list = []
    negative_list = []
    zero_list = []
    #Sort the Array
    arr.sort()

    #Append Values to Lists
    for value in arr:
        if value < 0:
            negative_list.append(value)
        elif value == 0:
            zero_list.append(value)
        elif value > 0:
            positive_list.append(value)
    #Calculate the Proportions of Negatives, Zeros, & Positives in the Original Array
    negative_proportion = format(len(negative_list)/len(arr), '.6f')
    zero_proportion = format(len(zero_list)/len(arr), '.6f')
    positive_proportion = format(len(positive_list)/len(arr), '.6f')

    return print(positive_proportion), print(negative_proportion), print(zero_proportion)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)