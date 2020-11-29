#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __area__ (self, length, width):
        self.length = length
        self.width = width
        a = self.length * self.width
        print(a)
        return a


class Circle:
    def __area__ (self, radius):
        self.radius = radius
        a = math.pi * self.radius**2
        print(a)
        return a

shape = Rectangle()
shape.__area__(3, 4)

shape1 = Circle()
shape1.__area__(2)

if __name__ == '__main__':  
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")