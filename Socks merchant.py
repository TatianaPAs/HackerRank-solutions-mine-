import math

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9


def sockMerchant(n, ar):
    count= 0
    #create a dictionary with unique color values and count them
    colours_count=(dict((i, ar.count(i)) for i in ar))
    
    #create a list of counted colours
    list1 = colours_count.values()
    
    #loop thru the list
    for x in list1:
        if x>1:
            #only values which divide by 2 can be counted
            y=math.floor(x/2)
            count+=y
        
        
    print(count)
    
    
        
    
sockMerchant(n, ar)


