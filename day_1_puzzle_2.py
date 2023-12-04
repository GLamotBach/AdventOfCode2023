# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 1 - Puzzle 2    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

def elf_cleaner(line):
    clean = line.replace("one", "o1e")
    clean = clean.replace("two", "t2o")
    clean = clean.replace("three", "t3e")
    clean = clean.replace("four", "4")
    clean = clean.replace("five", "5e")
    clean = clean.replace("six", "6")
    clean = clean.replace("seven", "7n")
    clean = clean.replace("eight", "e8t")
    clean = clean.replace("nine", "n9e")
    return clean


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
calibration_values = []

with open('day_1_puzzle_1_input.txt', 'r') as input_file:
    for line in input_file:
        line = elf_cleaner(line)
        digits_in_line = []
        for character in line:
            if character in digits:
                digits_in_line.append(character)
        number_in_line = int(digits_in_line[0] + digits_in_line[-1])
        calibration_values.append(number_in_line)

print(sum(calibration_values))

# TODO: Write an passive-aggressive e-mail to the elves regarding proper data formatting.  