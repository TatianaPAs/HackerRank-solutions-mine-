#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

grid = [["abc"],["ade"],["efg"]]
n=3


def gridChallenge(grid):
    for i in range(n):
        #sort every array in grid
       grid[i]=sorted(grid[i])
       #print (grid[i])
       #as length can be different to N in some cases, better to get length of first grid
    for i in range(len(grid[0])):
        col=[]
        #get the column items
        for j in range(n):
            col.append(grid[j][i])
            #if column not sorted, return no, else yes
        if col!=sorted(lst):
            return 'NO'
    return 'YES'
        
                   

                  
    
        
        
print(gridChallenge(grid))