
year=1800

def dayOfProgrammer(year):


    if year<1918:
        if year % 4==0:
            return("12.09."+str(year))
        else:
            return("13.09."+str(year))
        
    if year>1918:
            if year%400==0 or( year%4==0 and year%100 !=0):
                return("12.09."+str(year))
            else:
                return("13.09."+str(year))
    else:
        return("26.09."+str(year))
    
  
    
print(dayOfProgrammer(year))