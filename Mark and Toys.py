prices=[1,12,5,111,200,1000,10]
k=50



def maximumToys(prices, k):
    # Write your code here
    #declare amount fo toys
    count=0
    #declare total spend
    totalSpend = 0
     
     #sort array
    prices.sort();
     #start byuing toys until can't buy anything else
    for i in prices:
        totalSpend+=i
        if (totalSpend<=k):
            i+=1
            count+=1
        else:
            totalSpend=totalSpend-i
            break
            
    return count

print(maximumToys(prices, k))