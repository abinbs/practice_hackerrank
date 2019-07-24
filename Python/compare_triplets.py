#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    p_alice=0
    p_bob=0
    for i in range(0,3):
        if a[i]<b[i]:
            p_bob=p_bob+1
        elif a[i]>b[i]:
            p_alice=p_alice+1
        else:
            p_alice=p_alice+0
            p_bob=p_bob+0
    return p_alice,p_bob    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
