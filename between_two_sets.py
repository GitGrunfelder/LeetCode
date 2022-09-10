from itertools import cycle

a = [2, 987]
b = [16, 32, 96]

largest = max(a)
t_max = largest # Temp var to prevent overwriting.
RUNNING = True
while RUNNING: # While true
    for num in cycle(a): # Cycle through array a, each item
        while t_max % num != 0: # While current t_max value doesn't divide evenly by current num in array
            t_max += largest # Increase temp max by original max value; Once this is no longer true:
        if all(t_max % num == 0 for num in a) is True: # Check if all items are true in the statement
            RUNNING = False # If so, set running to false, to end outer while loop.
            break # Break out of for loop.
print(t_max) # Give the value of the least common multiple.


# counter = 0
# for num in range(a[0],b[0]+1):
#     if any((num % i == 0 for i in a) and big % num == 0 for big in b):

#             counter+= 1
#             print(num)
# print(counter)






