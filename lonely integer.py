
a=[1,2,3,4,3,2,1]
def lonelyinteger(a):
    # Write your code here
    singlesArray = []
    for x in a:
        if x not in singlesArray:
            singlesArray.append(x)
            x+=1;
    return 2*sum(singlesArray)-sum(a)
                
            
       

print(lonelyinteger(a))
        