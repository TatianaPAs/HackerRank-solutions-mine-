# https://www.hackerrank.com/challenges/truck-tour/problem

N=3
petrolpumps=[[1,5],
             [10,3],
             [3,4]]



#[1,5] 1=ammount of petrol 5 = distance from this station to another
#you have no petrol
#1km=1liter of petrol

def truckTour(petrolpumps):
    #empty tank at the start
    petrol = 0
    #find ammount of tanks
    tanks = len(petrolpumps)
    #index if first station
    station=0
    index=station
    
    while index<tanks:
        
        #petrol adds petrol value minus km value
            petrol = petrol+petrolpumps[index][0]-petrolpumps[index][1]
            #if not enough petrol, start from another station
            if petrol<0:
                station+=1
                index=station
                petrol=0
            else:
                index+=1
    return station
            
        
        
print(truckTour(petrolpumps))       
        
            
        
            
    