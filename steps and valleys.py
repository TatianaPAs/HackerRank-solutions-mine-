
#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

steps=12
path=["DDUUDDUDUUUD"]



def countingValleys(steps, path):
    count=0
    valley=0
    stringPath="".join(path)
    for step in stringPath:
        
        if step == 'D':
            count-=1
        elif step=='U':
            count+=1;
            if count==0:
                valley+=1;
    return(valley)
            
        
    
    



print (countingValleys(steps, path))

