#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


s="middle-Outz"
k = 2
def caesarCipher(s, k):
    
    finalString = []
    lowerCaseA= ord('a')
    lowerCaseZ= ord('z')
    capitalA= ord('A')
    CapitalZ= ord('Z')
    
    for character in s:
        #check if it is a letter
        if character.isalpha():
            #set a new position for the letter, the original letter plus leftover of divison k
            newChar = ord(character)+k%26
            #chech position on break point
            if character.islower() and newChar>lowerCaseZ:
                finalString.append(chr(lowerCaseA-1+(newChar-lowerCaseZ)))
            elif character.isupper() and newChar>CapitalZ:
                finalString.append(chr(capitalA-1+(newChar-CapitalZ)))
            else:
                #if character not on a break point, add it new position
                finalString.append(chr(newChar))
        else:
            #if character not a letter, leave as is
            finalString.append(character)
            #put array to string
    return "".join(finalString)  
   
    
    
    
 
print(caesarCipher(s,k))