# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 9 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

sample = [13, 14, 13, 10, 5, -2, -11, -22, -35, -50, -67, -86, -107, -130, -155, -182, -211, -242, -275, -310, -347]


def extrapolate_value(list_of_values):
    all_sequences = []
    all_sequences.append(list_of_values)
    for sequence in all_sequences:
        new_sequence = []
        for value in range(len(sequence) - 1):
            new_value = sequence[value + 1] - sequence[value]
            new_sequence.append(new_value)
        all_sequences.append(new_sequence)
        check = len(new_sequence)
        for val in new_sequence:
            if val == 0:
                check -= 1
        if check == 0:
            break
    for value in reversed(range(len(all_sequences))):
        new_extrapolation = all_sequences[value][-1] + all_sequences[value - 1][-1]
        all_sequences[value - 1].append(new_extrapolation)
    return all_sequences[0][-1]


prepared_data = []
with open('day_9_input.txt', 'r') as import_file:
    for line in import_file:
        line = line.split()
        for value in range(len(line)):
            line[value] = int(line[value])
        prepared_data.append(line)

total = 0
for line in prepared_data:
    a = extrapolate_value(line)
    total += a

print(total)

#   *   *   *   *   *   *   *   *   *   *   *   *   Day 9 - Puzzle 2    *   *   *   *   *   *   *   *   *   *   *   *

def reverse_extrapolate_value(list_of_values):
    all_sequences = []
    all_sequences.append(list_of_values)
    for sequence in all_sequences:
        new_sequence = []
        for value in range(len(sequence) - 1):
            new_value = sequence[value + 1] - sequence[value]
            new_sequence.append(new_value)
        all_sequences.append(new_sequence)
        check = len(new_sequence)
        for val in new_sequence:
            if val == 0:
                check -= 1
        if check == 0:
            break
    for value in reversed(range(len(all_sequences))):
        new_extrapolation = all_sequences[value - 1][0] - all_sequences[value][0]
        all_sequences[value - 1].insert(0, new_extrapolation)
    return all_sequences[0][0]


prepared_data = []
with open('day_9_input.txt', 'r') as import_file:
    for line in import_file:
        line = line.split()
        for value in range(len(line)):
            line[value] = int(line[value])
        prepared_data.append(line)

total = 0
for line in prepared_data:
    a = reverse_extrapolate_value(line)
    total += a

print(total)

