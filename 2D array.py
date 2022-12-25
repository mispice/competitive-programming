#!/bin/python3

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

def hourglassSum(arr):
    # Write your code here
    result = -math.inf
    for row in range(4):
        for col in range(4):
            sumation = 0
            sumation = (arr[row][col] + arr[row][col+1] +
            arr[row][col+2]+arr[row+1][col+1]
            + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2])
            result = max(result,sumation)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
