#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #Multiply the Count of a in s by the Ratio of n to the Length of s
    repeat_count = s.count('a') * math.floor(n / len(s))
    #print(f"Length of s: {len(s)}")
    #print(f"repeat_count: {repeat_count}")
    #Calculate the Remainder of n Divided by the Length of s
    mod = n % len(s)
    #print(f"remainder of last_string: {mod}")
    #Create a List of the Final String Up to the Modulus Index
    mod_list = list(s)[0:mod]
    #Create a Count of a in last_count
    last_count = mod_list.count('a')
    #print(f"last_count: {last_count}")

    #Count the Number of a's in string_list
    a_count = repeat_count + last_count
    #print(a_count)
    return a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()