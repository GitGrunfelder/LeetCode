#
import itertools

# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# Find sub array of longest length where all ints
# have a difference of absolute value =< 1
# In a = [1,1,2,2,4,4,5,5,5], that subarray would be
# 4,4,5,5,5
# a = [4, 6, 5, 3, 3, 1]
# a = [1, 1, 2, 2, 4, 4, 5, 5, 5]

from typing import Counter
def pickingNumbers(a):
    currentMax = 0
    counted_a = Counter(a)
    for k,v in counted_a.items():
        if abs(k-(k-1)) <= 1: # Then this is difference of 1 or less. Can be counted
            print(k-1)
            if (counted_a[k] + counted_a[k-1]) > currentMax: # If (number in array + (number in array - 1)) 
                currentMax = counted_a[k] + counted_a[k-1] # If only one type of number in array, it will end up only returning count of that number.
    return currentMax
    
            
print(pickingNumbers(a))
