#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    #Initialize the Cloud List Position & Number of Jumps
    cloud = 0
    jumps = 0
    #Loop Through the Cloud List
    while cloud < len(c):
        #print(f"The cloud number is: {cloud}")
        if cloud < len(c) - 2:
            if c[cloud + 1] == 0:
                if c[cloud + 2] == 0:
                    cloud += 2
                    jumps += 1
                    #print(f"There is a jump of 2 spaces.")
                elif c[cloud + 1] == 0:
                    cloud += 1
                    jumps += 1
                    #print(f"There is a jump of 1 space.")
            elif c[cloud + 1] == 1:
                cloud += 1
                #print(f"There is a jump that skips a space.")
                if c[cloud + 1] != 1:
                    cloud += 1
                    jumps += 1
                    #print(f"There is a jump of 1 space.")
        elif cloud == len(c) - 2:
            if c[cloud + 1] == 0:
                cloud += 1
                jumps += 1
                #print(f"There is a jump of 1 space.")
            elif c[cloud + 1] == 1:
                cloud += 1

        elif cloud == len(c) - 1:
            break
    print(f"The number of jumps is: {jumps}")
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()