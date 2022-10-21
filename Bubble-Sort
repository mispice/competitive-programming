#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a): # Write your code here
    # Write your code here
    counter = 0
    length = len(a)
    for i in range(length):
        if sorted(a) == a:
            break
        for x in range(length-1):
            if a[x]>a[x+1]:
                a[x],a[x+1] = a[x+1], a[x]
                counter +=1
    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[length-1]}")
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
