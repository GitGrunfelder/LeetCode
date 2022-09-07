# Given an array of distances that apples/oranges fall
# Determine how many fall within range that represents
# a house. 
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_counter = 0
    orange_counter = 0
    for apple in apples:
        if (apple + a) in range(s, t+1):
            apple_counter += 1
    for orange in oranges:
        if (orange + b) in range(s, t+1):
            orange_counter += 1
    print(apple_counter)
    print(orange_counter)