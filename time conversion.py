
s=("12:59:59AM")

s=("10:45:54AM")
def timeConversion(s):
    # Find where is Am or Pm
    AP=s[-2]
    
    # find where is hour number
    hour=int(s[0:2])
    #if time starts with P (afternoon time)
    if AP=="P":
        # do not change if it is 12
        if hour==12:
            time=s[0:-2]
        else:
            #add 12 if it is not 12
            hourP=hour+12
            time=str(hourP)+s[2:-2]
    else:
        # if it is a morning time
        #if starts wil 12 convert hour to 00
        if hour==12:
            hourA=str("00")
            time=hourA+s[2:-2]
        else:
            # if not 12 print as is without AM saign
            time=s[0:-2]
    return time
    
   
print (timeConversion(s))

