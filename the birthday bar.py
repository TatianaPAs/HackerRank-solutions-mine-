s=[4,1]
d=4
m=1


def birthday(s, d, m):
    length = m
    total=0
    if m>len(s):
        total=0
    elif m==len(s):
        if sum(s)!=d:
            total=0
        else:
            total=1
    else:
        for i in range(0,len(s)+1-m):
            if sum(s[i:i+m]) == d:
                total+=1
            
            
    return total
        
print(birthday(s, d, m))       
   
        