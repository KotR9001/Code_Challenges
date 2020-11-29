#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(1, n+1):
        if i %3 == 0 and i %5 == 0:
            message = print('FizzBuzz')
        elif i %3 == 0 and i %5 != 0:
            message = print('Fizz')
        elif i %3 != 0 and i %5 == 0:
            message = print('Buzz')
        elif i %3 != 3 and i %5 != 0:
            message = print(i)
    return message

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)