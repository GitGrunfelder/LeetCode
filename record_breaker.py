'''Given a list of scores for the season, return a list of how many times the max and min score were broken in all games.'''
scores = [5, 10,25,4,56,23,10,2]

min_score = scores[0]
max_score = scores[0]
broke_min = 0
broke_max = 0
for index, score in enumerate(scores):

    if score < min_score:
        min_score = scores[index]
        broke_min += 1
    elif score > max_score:
        max_score = scores[index]
        broke_max += 1
    else:
        continue
print(f'{broke_max} {broke_min}')


