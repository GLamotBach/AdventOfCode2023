# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 10 - Puzzle 1   *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

map = []

with open('day_10_input.txt', 'r') as import_file:
    for line in import_file:
        map.append(line)


def find_startpoint(map):
    for line_nr in range(len(map)):
        for column_nr in range(len(map[line_nr])):
            if map[line_nr][column_nr] == 'S':
                startpoint = [line_nr, column_nr]
                return startpoint



start = find_startpoint(map)
print(start)
top_directions = ['7', '|', 'F']
bottom_directions = ['|', 'L', 'J']
left_directions = ['F', '-']
right_directions = ['7', '-']

position = [0, 0]
position[0] = start[0]
position[1] = start[1]
direction = 'horizontal'
steps = 0
path = []
path.append(start)
previous_position = [0, 0]

if map[position[0] - 1][position[1]] in top_directions:
    previous_position[0] = position[0]
    previous_position[1] = position[1]
    position[0] -= 1
    steps += 1
elif map[position[0]][position[1] - 1] in left_directions:
    previous_position[0] = position[0]
    previous_position[1] = position[1]
    position[1] -= 1
    steps += 1
elif map[position[0]][position[1] + 1] in right_directions:
    previous_position[0] = position[0]
    previous_position[1] = position[1]
    position[1] += 1
    steps += 1
elif map[position[0] + 1][position[1]] in bottom_directions:
    previous_position[0] = position[0]
    previous_position[1] = position[1]
    position[0] += 1
    steps += 1

print(position)
path.append(position)
print(path)

while position[0] != start[0] or position[1] != start[1]:

    if map[position[0]][position[1]] == '|':
        destination_1 = [position[0] - 1, position[1]]
        destination_2 = [position[0] + 1, position[1]]
    elif map[position[0]][position[1]] == '-':
        destination_1 = [position[0], position[1] - 1]
        destination_2 = [position[0], position[1] + 1]
    elif map[position[0]][position[1]] == 'L':
        destination_1 = [position[0] - 1, position[1]]
        destination_2 = [position[0], position[1] + 1]
    elif map[position[0]][position[1]] == 'J':
        destination_1 = [position[0] - 1, position[1]]
        destination_2 = [position[0], position[1] - 1]
    elif map[position[0]][position[1]] == '7':
        destination_1 = [position[0] + 1, position[1]]
        destination_2 = [position[0], position[1] - 1]
    elif map[position[0]][position[1]] == 'F':
        destination_1 = [position[0] + 1, position[1]]
        destination_2 = [position[0], position[1] + 1]


    if destination_1[0] == previous_position[0] and destination_1[1] == previous_position[1]:
        previous_position = position
        position = destination_2
        path.append(position)
        steps += 1
    elif destination_2[0] == previous_position[0] and destination_2[1] == previous_position[1]:
        previous_position = position
        position = destination_1
        path.append(position)
        steps += 1


print((len(path) - 1)/2)

#   *   *   *   *   *   *   *   *   *   *   *   *   Day 10 - Puzzle 2   *   *   *   *   *   *   *   *   *   *   *   *

map_2 = []
for row in range(len(map)):
    nodes_in_row = []
    for column in range(len(map[row])):
        checked_node = [row, column]
        if checked_node in path:
            nodes_in_row.append(column)
    map_2.append(nodes_in_row)

for n in map_2:
    print(n)


