
arr=[1,4,4,4,5,3]

def migratoryBirds(arr):
    count=0
    appearance=1
    birds=[]
  #only birds with numbers 1-5 can be in the array  
    for x in range(0,6):
        count = arr.count(x)
    #create a list of their appearance
        birds.append(count)
        x+=1
    #loop thru the list
    for i in birds:
  #check if bird apears more than once
        if i>appearance:
            appearance=i
            i+=1
        #find number of the bird
            bird_number=birds.index(appearance)
    return bird_number
        
    
                
                         
  
     
   
    
print(migratoryBirds(arr))
   