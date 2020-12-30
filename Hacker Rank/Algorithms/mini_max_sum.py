#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    #Create a List for Sums
    sum_list = []
    #Create a List for Subsequence Lists
    subsequence_list_list = []

    #Loop Through the Array
    for i in range(len(arr)):
        #Create an Empty Subsequence List
        subsequence_list = []
        #Loop Through the Array Again
        for j in range(len(arr)):
            if i != j:
                subsequence_list.append(arr[j])
        subsequence_list_list.append(subsequence_list)
    #print(subsequence_list_list)

    #Calculate the Sum of Each Subsequence
    for subsequence in subsequence_list_list:
        sum = 0
        for element in subsequence:
            sum += element
        sum_list.append(sum)

    #Calculate the Minimum & Maximum Subsequence Sums
    min_sum = min(sum_list)
    max_sum = max(sum_list) 
    return print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)