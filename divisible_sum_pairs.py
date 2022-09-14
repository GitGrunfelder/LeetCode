''''Count the number of pairs in an array that have sums that are
 evenly divisible by a given number.'''

list_of_nums = [1, 3, 2, 6, 1, 2]
# This is the number we want the sum of the pairs divisible by.
K = 3
# This is the length of the array.
N = 6
count = 0
for index, num in enumerate(list_of_nums): # Gather index and value for each item in array
    for i in list_of_nums[index+1:]: # For each value in array in range of (current index + 1) to end of array
        if (num + i) % K == 0: # If sum of current number and current inner loop value are divisible by K evenly
            count += 1 # Tally
            print(num, i)# This prints each pair, mainly for debugging.           
print(count)
#edit
