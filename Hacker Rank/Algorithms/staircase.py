#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for step in range(0, n):
        if step < n:
            print(((n-step-1) * ' ') + ((step + 1) * '#'))

if __name__ == '__main__':
    n = int(input())

    staircase(n)