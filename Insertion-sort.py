#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    alternate = 0
    for i in reversed(range(n)):
        if arr == sorted(arr):
           print(' '.join((map(str,arr))))
           break
        elif arr[i] < arr[i-1]:
            alternate = arr[i]
            arr[i] = arr[i-1]
            print(' '.join(map(str,arr)))
            arr[i-1] = alternate
         
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
