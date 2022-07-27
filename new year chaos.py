#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

q=[1,2,3,5,4,6,7,8]

def minimumBribes(q):
    # Write your code here
    bribes=0
    position1=1
    position2=2
    position3=3
    for i in range(0,len(q)):
        if q[i]==position1:
                position1=position2
                position2=position3
                position3+=1
        elif q[i]==position2:
            bribes+=1
            position2=position3
            position3+=1
        elif q[i] == position3:              
            bribes+=2
            position3+=1
        else:
            print("Too chaotic")
            retrun
            
    print(bribes)
            
minimumBribes(q)                   
                
                

