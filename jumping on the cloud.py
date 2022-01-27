c=[0,0,0,1,0,0]
n=6
def jumpingOnClouds(c):
    
    #define jumps and position of the player
    jump=0
    place=0
    
    #if position of the player 2 steps before the end:
    while place<(len(c)-2):
        
        #if he can jump over 2 clouds, increase place to 2
        if c[place+2]==0:
            place+=2
        else:
            
          #if he can't jump over two, increase by 1  
            place+=1
        jump+=1
        
        #if only 1 cloud left he can do only 1 jump
    if place!=(len(c)-1):
        jump+=1
            
    return jump
    
    
    
    
    
print(jumpingOnClouds(c));