# Given an array of 5 ints, print max value and min value
# of any 4 ints in the array.
def miniMaxSum(arr):
    sorted_arr = sorted(arr) # By sorting, the array is always ascending.
    min_sum = sum(sorted_arr[:-1]) # By calculating sum of first 4 items, that must be minimum.
    max_sum = sum(sorted_arr[1:]) # Last 4 in an ascending array must be max.
    print(f'{min_sum} {max_sum}')