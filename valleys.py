'''Given a sequence of ups and downs, with each step being 1 unit of altitude,
determine how many valleys are entered and exited. Valley defined as area lower than sea level,
ends when back at sea level.'''

steps = 8 # Number of ups and downs
path = ['D','D','U','U','D','D','U','D','U','U','U','D']
'''
This function checks whether currently in valley, keeps track of valley count, and checks altitude.
For each step, if UP, increase altitude by 1. (else decrease by 1)
    If altitude is negative;
        If not in valley already;
        add 1 to valley counter
        set in valley to true
        check if at sea level, if so, no longer in valley
        break while in valley loop
    if altitude not negative (>= 0 )
        not in valley.
return total valley count
        '''
def countingValleys(steps, path): 
    altitude = 0
    valley_count = 0
    in_valley = False
    for i in path:
        if i == 'U':
            altitude += 1
        else:
            altitude -= 1
            
        if altitude < 0:
            while in_valley is False:
                valley_count += 1
                in_valley = True
                if altitude == 0:
                    in_valley = False
                break
        else:
            if altitude == 0:
                in_valley = False
    return valley_count


# Iteration
'''This function is more compact and straightforward. 
For each item, if up increase altitude, otherwise decrease.
If current altitude (after stepping) is sea level(0) and the step was UP,
then you just exited a valley, increase count by 1.'''
def countingValleys(steps, path):
    sea_level = 0
    altitude = 0
    valley_count = 0
    for i in path:
        if i == 'U':
            altitude += 1
        else:
            altitude -= 1
        if altitude == sea_level and i == 'U':
            valley_count += 1
        
    return valley_count


print(countingValleys(steps, path))
        


    