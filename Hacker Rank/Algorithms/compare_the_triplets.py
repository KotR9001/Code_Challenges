#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_sum = 0
    bob_sum = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                if a[i] > b[j]:
                    alice_sum += 1
                elif a[i] < b[j]:
                    bob_sum += 1
                else:
                    alice_sum += 0
                    bob_sum += 0
    return alice_sum, bob_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()