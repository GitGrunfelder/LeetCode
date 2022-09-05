# For whatever n, print a staircase as high and wide, must be no spaces on bottom row.
def staircase(n):
    spaces = (n-1) # Starts spaces at 1 less than max.
    for i in range(n):
        print((' '* spaces) + ('#' * (i+1))) # Prints ' ' for as many spaces as current.
                                             # Concatenates with # * current count + 1
        spaces -= 1 # Reduce number of spaces
        
staircase(10)