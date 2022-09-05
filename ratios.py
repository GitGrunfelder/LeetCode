# Function to find ratio of pos/neg/and zero in array of numbers. Formatted to 6th decimal.
def plus_minus(arr):
    
    pos_count = 0
    neg_count = 0
    zero_count = 0

    for i in arr:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1
        else:
            zero_count += 1

    print(f'{(pos_count/len(arr)):.6f}')
    print(f'{(neg_count/len(arr)):.6f}')
    print(f'{(zero_count/len(arr)):.6f}')

def plus_minus_v2(arr):

    print(f'{sum([1 for i in arr if i > 0])/len(arr):.6f}')
    print(f'{sum([1 for i in arr if i < 0])/len(arr):.6f}')
    print(f'{sum([1 for i in arr if i == 0])/len(arr):.6f}')


array = [1, 1, 0, -1, -1]
plus_minus(array)
plus_minus_v2(array)