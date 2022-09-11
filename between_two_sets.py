# from itertools import cycle
from collections import Counter
import math

a = [3, 4]
b = [24, 48]
all_prime_factors = []
counts = {}

# Break down items in a to prime factors
def prime_factorization(x):
    prime_factors = [] # Add all values that are prime factors of x
    divisor = 2 # Start at lowest prime number
    while divisor <= x: # If x is 1, function complete.
        if x % divisor == 0: # If x divided by current divisor leaves no remainder
            prime_factors.append(divisor) # That divisor is a prime factor, add it to list.
            x = x/divisor # number is updated to new value after dividing.
        else:
            divisor += 1 # If not divisible by 2, increase by 1, until next prime factor is hit.
    return prime_factors

# Not sure if I should include this in a function, just adds all factor lists to a bigger list.
for num in a:
    all_prime_factors.append(prime_factorization(num))

# This checks each list for a count of each item, assigns to dictionary, and if one factor list has a higher count,\
# replaces that key with a higher value.
def find_commons():
    for list in all_prime_factors:
            counted = Counter(list)
            for i in counted:
                if counted[i] > counts.get(i,0):
                    counts[i] = counted[i]
    return counts
find_commons()
# This creates a list of all factors to the power of # of times they appear most in any list.
def find_lcm():
    to_the_power = []
    for factor, power in counts.items():
        to_the_power.append(factor ** power)
    lcm = math.prod(to_the_power) # math function gives product of new list.
    return lcm

counter = 0
for num in range(find_lcm(), min(b)+1):
    if all(num % i == 0 for i in a) and all(i % num == 0 for i in b) is True:
        counter += 1
print(counter)