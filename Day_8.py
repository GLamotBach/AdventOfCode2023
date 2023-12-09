# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 8 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *


# Data preparation
with open('day_8_input_directions.txt', 'r') as import_file_1:
    for line in import_file_1:
        map_directions = line

nodes = {}
with open('day_8_input_nodes.txt', 'r') as import_file_2:
    for line in import_file_2:
        line = line.replace('\n', '')
        line = line.replace(',', '')
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace('=', '')
        line = line.split(' ')
        nodes[line[0]] = [line[2], line[3]]

steps = 0
current_node = 'AAA'
while current_node != 'ZZZ':
    for direction in map_directions:
        if direction == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        steps += 1

print(steps)

