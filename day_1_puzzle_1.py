# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 1 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
calibration_values = []

with open('day_1_puzzle_1_input.txt', 'r') as input_file:
    for line in input_file:
        digits_in_line = []
        for character in line:
            if character in digits:
                digits_in_line.append(character)
        number_in_line = int(digits_in_line[0] + digits_in_line[-1])
        calibration_values.append(number_in_line)

print(sum(calibration_values))





