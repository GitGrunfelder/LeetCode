# 2 kangaroos start at x1 and v1
# x2 and v2 are the respective distance of hops
# check if they will match up. (range of 10k)

def kangaroo(x1, v1, x2, v2):
    kang1 = x1 + v1 # First hop from starting position
    kang2 = x2 + v2 # First hop from starting position
    for i in range(10000): # For 10k iterations
        if v2 >= v1: # First check that that kangaroo that started ahead doesn't have greater hop distance
            return('NO')
        elif (kang1) == (kang2): # Next check if currently in same spot.
            return('YES')
        kang1 += v1 # Add a hop
        kang2 += v2 # Add a hop
    return('NO') # If after 10k loop no value returned, answer is no.
