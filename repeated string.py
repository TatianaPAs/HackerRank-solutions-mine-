
s="a"
n=1000000000000

def repeatedString(s, n):
    count=0
    count1=0
    #count how many times will pattern repeat
    repeats = n//len(s)
   
    for x in s:
        if x=="a":
            count+=1
            
    #find how many times A in the leftover pattern      
    for x in s[:n % len(s)]:
        if x=="a":
            count1+=1
            
    finalCount=count*repeats+count1
    return finalCount
    
            
    


print(repeatedString(s, n));     
            
        