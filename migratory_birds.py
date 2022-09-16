from collections import Counter

# Determine which type of bird in a flock occurs at the highest frequency.
birds = [1, 1, 2, 2, 3]
def migratoryBirds(arr):
    current_max = 0
    bird_id = 0
    counted_birds = Counter(arr)
    for id, count in counted_birds.items():
        if count > current_max:
            current_max = count
            bird_id = id
        elif count == current_max and id < bird_id:
            bird_id = id
    return bird_id
  
print(migratoryBirds(birds))