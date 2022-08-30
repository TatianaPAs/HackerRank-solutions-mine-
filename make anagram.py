
a="aabcddda"
b="abbbbcdaa"



def makeAnagram(a, b):
    #declare empty string
    c=[]
    #find total length of both strings
    lenght=len(a)+len(b)
    for x in a:
        if x in b:
            # if letter in both a and b string,
            # add it to c and remove from b
            c.append(x);
            b=b.replace(x,'',1)
            continue
            
            
    #from total length remove 2 lengths of c 
    result = lenght-2*len(c)
    print(result)
    
    

    
makeAnagram(a, b)