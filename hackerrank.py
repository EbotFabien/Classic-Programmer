import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
        c=[0,0]
        if a[0] > b[0]:
            c[0]=c[0]+1
        elif a[0] < b[0]:
            c[0] =c[0]-1
            c[1] =c[1]+1
        if a[1] > b[1]:
            c[0]=c[0]+1
        elif a[1] < b[1]:
            c[0] =c[0]-1
            c[1] =c[1]+1
        if a[2] > b[2]:
            c[0]=c[0]+1
        elif a[2] < b[2]:
            c[0] =c[0]-1
            c[1] =c[1]+1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
