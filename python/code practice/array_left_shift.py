#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

'''
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
For example, if 2 left rotations are performed on array[1,2,3,4,5], then the array would become [3,4,5,1,2]. 
Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a of n integers and a number, d, perform d left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.
'''

# a = array
# d = how many left shifts
# n = array length
def rotLeft(a, d):
    shifted_arr = []

    for value in a[d:]:
        print(value)
        shifted_arr.append(value)

    for value in a[:d]:
        shifted_arr.append(value)

    return shifted_arr


if __name__ == '__main__':
    n = 10
    d = 5
    a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77]

    result = rotLeft(a, d)
    print(result)