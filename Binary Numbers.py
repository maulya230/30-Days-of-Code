#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a=[]
    while n>0:
        b=n%2
        n=n//2
        a.append(b)
    count,result=0,0
    for i in range(0,len(a)):
        if a[i] == 0:
            count = 0
        else:
            count +=1
            result = max(result,count)
        
    print(result)
        
