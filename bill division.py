k=1
bill=[3,10,2,9]
b=12



def bonAppetit(bill, k, b):
    total=0
    
    #remove the item from the list, which she did not eat
    bill.pop(k)

    for x in bill:
    #sum atems and divide by 2
        total+=x/2
        x+=1
    if total==b:
        print("Bon Appetit")
    else:
    #result must be integer
        print(int(b-total))
    
    
bonAppetit(bill, k, b)      
    
        