# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 11 - Puzzle 1   *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

star_map = []
empty_rows = []
with open('day_11_input.txt', 'r') as import_file:
    for line in import_file:
        new_line = []
        line = line.replace('\n', '')
        for l in line:
            new_line.append(l)
        star_map.append(new_line)
        if '#' not in line:
            additional_line = new_line.copy()
            star_map.append(additional_line)

empty_columns = []
for column in range(len(star_map[0])):
    galaxies_in_row = 0
    for row in range(len(star_map)):
        if star_map[row][column] == '#':
            galaxies_in_row += 1

    if galaxies_in_row == 0:
        empty_columns.append(column)

empty_columns.sort(reverse=True)

for row in range(len(star_map)):
    for i in empty_columns:
        star_map[row].insert(i + 1, '.')

galaxies = []
for row in range(len(star_map)):
    for column in range(len(star_map[row])):
        if star_map[row][column] == '#':
            galaxies.append([row, column])

pairs = []

for a in range(len(galaxies)):
    galaxy_a = galaxies[a]
    for b in range(a + 1, len(galaxies)):
        galaxy_b = galaxies[b]
        pair = [galaxy_a, galaxy_b]
        pairs.append(pair)

total = 0

for pair in pairs:
    x = abs(pair[0][0] - pair[1][0])
    y = abs((pair[0][1] - pair[1][1]))
    distance = x + y
    total += distance

print(f"Part 1: {total}")

#   *   *   *   *   *   *   *   *   *   *   *   *   Day 11 - Puzzle 2   *   *   *   *   *   *   *   *   *   *   *   *

star_map = []
empty_rows = []
empty_columns = []
multiplier = 999999

with open('day_11_input.txt', 'r') as import_file:
    for line in import_file:
        new_line = []
        line = line.replace('\n', '')
        for l in line:
            new_line.append(l)
        star_map.append(new_line)
        if '#' not in line:
            empty_rows.append(len(star_map) - 1)

for column in range(len(star_map[0])):
    galaxies_in_row = 0
    for row in range(len(star_map)):
        if star_map[row][column] == '#':
            galaxies_in_row += 1
    if galaxies_in_row == 0:
        empty_columns.append(column)

galaxies = []
for row in range(len(star_map)):
    for column in range(len(star_map[row])):
        if star_map[row][column] == '#':
            galaxies.append([row, column])

pairs = []

for a in range(len(galaxies)):
    galaxy_a = galaxies[a]
    for b in range(a + 1, len(galaxies)):
        galaxy_b = galaxies[b]
        pair = [galaxy_a, galaxy_b]
        pairs.append(pair)

total = 0

for pair in pairs:
    x = abs(pair[0][0] - pair[1][0])
    y = abs((pair[0][1] - pair[1][1]))
    distance = x + y

    for empty_row in empty_rows:
        if pair[1][0] > empty_row > pair[0][0] or pair[1][0] < empty_row < pair[0][0]:
            distance += multiplier

    for empty_column in empty_columns:
        if pair[0][1] > empty_column > pair[1][1] or pair[0][1] < empty_column < pair[1][1]:
            distance += multiplier

    total += distance

print(f"Part 2: {total}")