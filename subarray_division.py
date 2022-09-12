'''Given an array of integers, find the number of subarrays of length
m having sum d.'''

chocolate_bar = [1, 3, 5, 5, 5, 4,5, 1, 1, 4]
m = 4 # Check through each subarray of len 4
d = 19 # and see if those items in the 4 subarray sums to 19

def birthday(s, d, m):
    
    count = 0 
    for index, num in enumerate(s): # Track index and value at index
        if sum(s[index:index+m]) == d: # If the sum of s[at this range of current index:index+m] is == d
            count += 1 # if so, add a tally
    return count # return the total times the event occurs.
    