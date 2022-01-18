#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    arrstr=str(ar)
    newarr=arrstr[1:-1]
    listarr=list()
    result=0
    #for i in newarr:
     #   listarr.append(i)
    for i in ar:
        result=result+ int(i)
   # for i in listarr:
    #    result=result+ int(i)

    return result
    #
    # Write your code here.
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
