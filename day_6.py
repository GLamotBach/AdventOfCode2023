# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 5 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

# Input:

time = [48, 93, 84, 66]
distance = [261, 1192, 1019, 1063]


def race_boat(t, d):
    win = []
    for speed in range(1, t):
        time_left = t - speed
        distance_traveled = speed * time_left
        if distance_traveled > d:
            win.append(speed)
    return len(win)

all_wins = []
for n in range(len(time)):
    all_wins.append(race_boat(time[n], distance[n]))

print(all_wins)

score = 1
for j in all_wins:
    score = score * j
print(score)

print(race_boat(48938466, 261119210191063))