import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zero=0
    v_neg=0
    v_pos=0
    v_zero=0
    t=n
    for i in range (0,n):
        if arr[i]>0:
            pos=pos+1
        elif arr[i]<0:
            neg=neg+1
        else:
            zero=zero+1
    v_pos=pos/t
    v_neg=neg/t
    v_zero=zero/t
    print (v_pos)
    print (v_neg)
    print (v_zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
