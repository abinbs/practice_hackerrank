

import math
import os
import random
import re
import sys
import string


def solve(s):  #(Function is to capitalise first letter of each word )
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()  #(Input a string)

    result = solve(s)  #(Function is called by passing the parameter s)

    fptr.write(result + '\n')

    fptr.close()
