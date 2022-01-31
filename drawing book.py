n=6
p=2



def pageCount(n, p):
    pagesFromFront=int((p//2))
    pagesFromBack=int((n-p)//2)
    if n == 2:
        return 0
    if n % 2 == 0 and n-p == 1:
        return 1
    if pagesFromFront>pagesFromBack:
        return pagesFromBack
    else:
        return pagesFromFront
    
    
    
    
print (pageCount(n, p))