# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 12 - Puzzle 1   *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
import itertools


def check_configuration(combination, sequences):
    working_in_row = 0
    working_sequence = []
    for node in range(len(combination)):
        if combination[node] == '#' and node == (len(combination) - 1):
            working_in_row += 1
            working_sequence.append(working_in_row)
        elif combination[node] == '#':
            working_in_row += 1
        elif combination[node] == '.' and working_in_row > 0:
            working_sequence.append(working_in_row)
            working_in_row = 0
    if len(working_sequence) == len(sequences):
        for i in range(len(sequences)):
            if working_sequence[i] != sequences[i]:
                return False
        return True
    return False


def make_list(string):
    new_list = []
    for c in string:
        new_list.append(c)
    return new_list


def check_possible_configurations(springs, sequences):
    possible_configurations = 0
    unknown = []
    for i in range(len(springs)):
        if springs[i] == '?':
            unknown.append(i)
    working_known = springs.count('#')
    working_count = sum(sequences)
    working_unknown = working_count - working_known
    comb = itertools.combinations(unknown, working_unknown)
    springs = springs.replace('?', '.')
    springs = make_list(springs)
    for combination in comb:
        attempt = springs.copy()
        for c in combination:
            attempt[c] = '#'
        if check_configuration(attempt, sequences):
            possible_configurations += 1
    return possible_configurations


springs = []
sequences = []
with open('day_12_input.txt', 'r') as import_file:
    for line in import_file:
        line = line.split()
        seq = line[1].split(',')
        seq_2 = []
        for s in seq:
            seq_2.append(int(s))
        springs.append(line[0])
        sequences.append(seq_2)

total_count = 0
for i in range(len(springs)):
    row = check_possible_configurations(springs[i], sequences[i])
    total_count += row

print(f"Part 1: {total_count}")

