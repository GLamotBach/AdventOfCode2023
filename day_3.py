# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *///\\\ *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 3 - Puzzle 1    *   *   *   *   *   *  ///\\\   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  ||   *   *   *   *   *

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('day_3_input.txt', 'r') as import_file:
    # Finding out what symbols we are working with. And creating a matrix on which we will be working on
    symbol_list = []
    matrix = []
    for line in import_file:
        row = []
        for character in line:
            row.append(character)
            if character not in symbol_list:
                symbol_list.append(character)
        matrix.append(row)
    symbol_list.remove('.')
    symbol_list.remove('\n')
    for digit in digits:
        symbol_list.remove(digit)

part_numbers = []

row_index = 0
for row in matrix:
    number = []
    column_index = 0
    for character in row:
        if len(number) == 0:
            if character in digits:
                number.append(character)
        else:
            if character in digits:
                number.append(character)
            else:
                # Fields to be checked for a part symbol
                l_of_number = len(number)
                fields_to_check = []
                # on left
                fields_to_check.append(matrix[row_index][column_index - (l_of_number + 1)])
                # on right
                fields_to_check.append(matrix[row_index][column_index])
                # above
                if row_index > 0:
                    for field in range(column_index - (l_of_number + 1), (column_index + 1)):
                        fields_to_check.append(matrix[row_index - 1][field])
                # under
                number_of_rows = len(matrix)
                if row_index < (number_of_rows - 1):
                    for field in range(column_index - (l_of_number + 1), (column_index + 1)):
                        fields_to_check.append(matrix[row_index + 1][field])

                for field in fields_to_check:
                    if field in symbol_list:
                        part_number = ""
                        for n in number:
                            part_number += n
                        part_number = int(part_number)
                        part_numbers.append(part_number)
                number = []
        column_index += 1
    row_index += 1

print(f"Part numbers: {sum(part_numbers)}")

# Part 2 - I'm starting to think that the elf may not be qualified for such repairs.


def number_reader(cords, matrix):
    start = matrix[cords[0]][cords[1]]
    start_cords = cords
    while start in digits:
        previous = [start_cords[0], start_cords[1] - 1]
        previous_val = matrix[previous[0]][previous[1]]
        start = previous_val
        if start in digits:
            start_cords = previous
    number = ""
    while matrix[start_cords[0]][start_cords[1]] in digits:
        number += matrix[start_cords[0]][start_cords[1]]
        start_cords = [start_cords[0], start_cords[1] + 1]
    return number


potential_gears = []
row_index = 0
for row in matrix:
    column_index = 0
    for column in row:
        if column == '*':
            gear_coordinates = [row_index, column_index]
            potential_gears.append(gear_coordinates)
        column_index += 1
    row_index += 1

gear_ratios = []

for gear in potential_gears:
    fields_to_check = []
    # Left
    left_field = [gear[0], gear[1] - 1]
    fields_to_check.append(left_field)
    # Right
    right_field = [gear[0], gear[1] + 1]
    fields_to_check.append(right_field)
    # Top
    top_field_l = [gear[0] - 1, gear[1] - 1]
    fields_to_check.append(top_field_l)
    top_field_c = [gear[0] - 1, gear[1]]
    fields_to_check.append(top_field_c)
    top_field_r = [gear[0] - 1, gear[1] + 1]
    fields_to_check.append(top_field_r)
    # Bottom
    bottom_field_l = [gear[0] + 1, gear[1] - 1]
    fields_to_check.append(bottom_field_l)
    bottom_field_c = [gear[0] + 1, gear[1]]
    fields_to_check.append(bottom_field_c)
    bottom_field_r = [gear[0] + 1, gear[1] + 1]
    fields_to_check.append(bottom_field_r)

    # Values of each field
    val_t_l = matrix[top_field_l[0]][top_field_l[1]]
    val_t_c = matrix[top_field_c[0]][top_field_c[1]]
    val_t_r = matrix[top_field_r[0]][top_field_r[1]]
    val_l = matrix[left_field[0]][left_field[1]]
    val_r = matrix[right_field[0]][right_field[1]]
    val_b_l = matrix[bottom_field_l[0]][bottom_field_l[1]]
    val_b_c = matrix[bottom_field_c[0]][bottom_field_c[1]]
    val_b_r = matrix[bottom_field_r[0]][bottom_field_r[1]]

    gear_numbers = []

    if val_t_l in digits and val_t_c in digits and val_t_r in digits:
        gear_numbers.append(number_reader(top_field_l, matrix))
    elif val_t_l in digits and val_t_c in digits:
        gear_numbers.append(number_reader(top_field_l, matrix))
    elif val_t_c in digits and val_t_r in digits:
        gear_numbers.append(number_reader(top_field_c, matrix))
    elif val_t_l in digits and val_t_r in digits:
        gear_numbers.append(number_reader(top_field_l, matrix))
        gear_numbers.append(number_reader(top_field_r, matrix))
    elif val_t_l in digits:
        gear_numbers.append(number_reader(top_field_l, matrix))
    elif val_t_c in digits:
        gear_numbers.append(number_reader(top_field_c, matrix))
    elif val_t_r in digits:
        gear_numbers.append(number_reader(top_field_r, matrix))

    if val_l in digits:
        gear_numbers.append(number_reader(left_field, matrix))

    if val_r in digits:
        gear_numbers.append(number_reader(right_field, matrix))

    if val_b_l in digits and val_b_c in digits and val_b_r in digits:
        gear_numbers.append(number_reader(bottom_field_l, matrix))
    elif val_b_l in digits and val_b_c in digits:
        gear_numbers.append(number_reader(bottom_field_l, matrix))
    elif val_b_c in digits and val_b_r in digits:
        gear_numbers.append(number_reader(bottom_field_c, matrix))
    elif val_b_l in digits and val_b_r in digits:
        gear_numbers.append(number_reader(bottom_field_l, matrix))
        gear_numbers.append(number_reader(bottom_field_r, matrix))
    elif val_b_l in digits:
        gear_numbers.append(number_reader(bottom_field_l, matrix))
    elif val_b_c in digits:
        gear_numbers.append(number_reader(bottom_field_c, matrix))
    elif val_b_r in digits:
        gear_numbers.append(number_reader(bottom_field_r, matrix))

    # Check if it is a gear
    if len(gear_numbers) == 2:
        ratio = int(gear_numbers[0]) * int(gear_numbers[1])
        gear_ratios.append(ratio)

print(f"Gear ratios: {sum(gear_ratios)}")






