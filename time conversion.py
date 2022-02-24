
s=("12:59:59AM")
def timeConversion(s):
    charX = s[-2]
    hour=int(s[0:2])

    if charX=="A":
        if hour !=12:
            time=s[:-2]
            return time
        else:
            y="00"
            time=str(y)+s[2:-2]
            return time
        
    elif charX!="A":
        x=int(s[0:2])+12
        time=str(x)+s[2:-2]
        return time
    
        
    
print (timeConversion(s))

