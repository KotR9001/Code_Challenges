#!/bin/python3

import os
import sys

#
# Complete the findPoint function below.
#
def findPoint(px, py, qx, qy):
    #
    if px < qx and py < qy:
        rx = 2 * qx - px
        ry = 2 * qy - py
    elif px < qx and py > qy:
        rx = 2 * qx - px
        ry = 2 * qy - py
    elif px > qx and py < qy:
        rx = 2 * qx - px
        ry = 2 * qy - py
    elif px > qx and py > qy:
        rx = 2 * qx - px
        ry = 2 * qy - py

    elif px == qx and py == qy:
        rx = px
        ry = py
    elif px == qx and py > qy:
        rx = px
        ry = 2 * qy - py
    elif px == qx and py < qy:
        rx = px
        ry = 2 * qy - py
    elif px > qx and py == qy:
        rx = 2 * qx - px
        ry = py
    elif px < qx and py == qy:
        rx = 2 * qx - px
        ry = py
    print(rx, ry)
    return rx, ry
    #

if __name__ == '__main__':
    #n = int(input())
    n = 10

    for n_itr in range(n):
        pxPyQxQy = input().split()
        #pxPyQxQy = [0, 0, 1, 1]
        #pxPyQxQy = [4, 3, 5, 2]
        #pxPyQxQy = [2, 4, 5, 6]
        #pxPyQxQy = [1, 2, 2, 2]
        #pxPyQxQy = [1, 1, 1, 1]
        #pxPyQxQy = [1, 2, 2, 1]
        #pxPyQxQy = [1, 8, 7, 8]
        #pxPyQxQy = [9, 1, 1, 1]
        #pxPyQxQy = [8, 4, 3, 2]
        #pxPyQxQy = [7, 8, 9, 1]

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)
