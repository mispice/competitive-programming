#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    q = n//len(s)
    count_a_quotient = s.count('a')
    total_a_substr = q*count_a_quotient
    r = n%len(s)
    count_a_remainder = s[:r].count('a')
    total = total_a_substr + count_a_remainder
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
