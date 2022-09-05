def diagonalDifference(arr):
    primary = []
    secondary = []
    i = 0
    for line in arr:
        primary.append(line[i])
        i += 1
    print(primary)

    i = 0
    for line in arr:
        secondary.append(line[i-1])
        i -= 1
    print(secondary)

    primary_sum = 0
    for i, v in enumerate(primary):
        primary_sum += v

    secondary_sum = 0
    for i, v in enumerate(secondary):
        secondary_sum += v

    return abs(primary_sum - secondary_sum)

arr = [ [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12] ]

print(diagonalDifference(arr))


# Better way found after submitting my way.

def diagonalDifference(arr):
    # diag_r/diag_l to 0
    d_right = 0
    d_left = 0
    # for index / value in array
    for i, v in enumerate(arr):
        # from top left to bot right
        d_right += arr[i][i]
        # from top right to bot left
        d_left += arr[i][-(i+1)]
    return abs(d_right - d_left)
    
arr = [ [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12] ]
print(diagonalDifference(arr))