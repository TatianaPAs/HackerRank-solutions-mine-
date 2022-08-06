#A single string  that represents a time in -hour clock format (hh:mm:ssAM or hh:mm:ssPM).
time="06:05:45PM"
def timeConversion(s):
    # Write your code here
    if s[-2]=="A" and s[:2] !="12":
        return s[:-2]
    elif s[-2]=="A" and s[:2] =="12":
        newTime= "00"+s[2:-2]
        return newTime
    elif s[-2]=="P" and s[:2] !="12":
        hours = int(s[:2])
        eveningHours = hours+12
        eveningTime = str(eveningHours)+s[2:-2]
        return eveningTime
    else:
        return s[:-2]

print(timeConversion(time))
        
    