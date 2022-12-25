#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    result = 0
    i = 0
    length = len(c)
    while i<length:
            
        if length-i<=2:
            i+=1
            result+=1
        elif c[i+2] == 1:
            i+=1
            result+=1  
        elif c[i+2] == 0:
            i+=2
            result+=1
            
    return result-1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
