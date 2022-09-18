# From 1700-2700, determine the 256th day of any given year, accounting for changes
# in the calendar system and leap years.

# From 1700 - 1917, Julian Calendar was used, 
# Leap years were divisible by 4.

# 1918 transition to Gregorian Calendar, Jan 31st -> Feb 14th
# Leap years divisible by 400 OR divisible by 4 and NOT 100.

# Leap year - Feb has 29 days
# All other years, Feb has 28 days

# Given year (y), determine 256 day based on calendar at time.
# Print out as  dd.mm.yyyy
def dayOfProgrammer(year):
    non_leap_year = (f'13.09.{year}')
    leap_year = (f'12.09.{year}')
    non_leap_transition = (f'26.09.{year}')
    leap_transition = (f'27.09.{year}')
    
    
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            return leap_year
        else:
            return non_leap_year
    elif year == 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return leap_transition
        else:
            return non_leap_transition
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return leap_year
        return non_leap_year
    
print(dayOfProgrammer(1918))
    
    
        
        
        

