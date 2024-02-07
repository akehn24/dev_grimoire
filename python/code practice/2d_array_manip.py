#!/bin/python3

'''
I found this solution online after struggling. Having a hard time wrapping my brain around this problem and not sure
this even solves it.

https://www.codementor.io/@tower/hackerrank-hourglass-challenge-using-python-1ix7ftgbvu
'''

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
'''
An hourglass is a subset of values with indices falling in this pattern in 's graphical representation:
a b c 
  d 
e f g
There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6x6.
'''

def hourglassSum(arr):
    total_sum = 0
    hourglass_sum = 0
    for row in range(4):
        for col in range(4):
            top_sum = arr[row][col] + arr[row][col+1] + arr[row][col+2]
            mid_sum = arr[row+1][col+1]
            bot_sum = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            hourglass_sum = top_sum + mid_sum + bot_sum

            total_sum = max(total_sum, hourglass_sum)
        
    return total_sum

if __name__ == '__main__':
    rows, cols = (6, 6)
    arr = [[0]*cols]*rows

    arr[0] = [-9, -9, -9, 1, 1, 1]
    arr[1] = [0, -9, 0, 4, 3, 2]
    arr[2] = [-9, -9, -9, 1, 2, 3]
    arr[3] = [0, 0, 8, 6, 6, 0]
    arr[4] = [0, 0, 0, -2, 0, 0]
    arr[5] = [0, 0, 1, 2, 4, 0]

    '''
    Answer:
    -63, -34, -9, -12, 
    -10, 0, 28, 23, 
    -27, -11, -2, 10, 
    9, 17, 25, 18
    '''

    result = hourglassSum(arr)
    print(result)