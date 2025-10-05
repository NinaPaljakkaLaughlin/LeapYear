#create a function called "yearsize" that takes an int and returns the number
#of days for the given year
#should return 365 for a normal year and 366 for a leap year

def yearsize(year):
    #check if the year is a centennial for the exception
    if year % 100 == 0:
        if year % 400 == 0: #only if divisible by 400 it is a leap year
            return 366
        else:
            return 365
    elif year % 100 != 0:
        if year % 4 == 0:#any year divisible by 4 is a leap year
            return 366
        else:
            return 365
    
    


