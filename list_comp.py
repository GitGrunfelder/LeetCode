from collections import Counter

'''Given 3 points representing a cuboid on a 3D plain, 
find all combos of numbers within given point ranges whose sum != m (Use list comprehension)'''
x = 1
y = 1
z = 2
m = 3

permutations = [[i, j, k] for i in range(x+1)
                for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(permutations)


'''Find pairs of socks from ar, given each # represents a color.'''
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

def sockMerchant(n, ar):
    pairs = 0
    counted_sock_pairs = Counter(ar)
    for i in counted_sock_pairs.values():
        pairs += i//2
    return pairs

