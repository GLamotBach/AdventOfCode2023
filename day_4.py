# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 4 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

# Score for part 1
total_points = 0

# Matrix for part 2
matrix = []

with open('day_4_input.txt', 'r') as import_file:
    for card in import_file:
        matrix_row = []  # For part 2
        card = card.split("|")
        winning = card[0]
        winning = winning.split(":")
        winning = winning[1]
        winning = winning.split()
        matrix_row.append(winning)  # For part 2
        elfs_numbers = card[1]
        elfs_numbers = elfs_numbers.replace("\n", "")
        elfs_numbers = elfs_numbers.split()
        matrix_row.append(elfs_numbers)  # For part 2
        matrix.append(matrix_row)  # For part 2

        card_points = 0

        for number in elfs_numbers:
            if number in winning:
                if card_points == 0:
                    card_points += 1
                else:
                    card_points = card_points * 2

        total_points += card_points

print(f"Total score - Part 1: {total_points}")


# Part 2

cards = [x for x in range(1, 199)]
total_cards = 0

for card in cards:
    card_winnings = matrix[card - 1][0]
    card_numbers = matrix[card - 1][1]
    card_score = 0
    for number in card_numbers:
        if number in card_winnings:
            card_score += 1
    for i in range(card_score):
        cards.append(card + i + 1)
    total_cards += 1

print(f"Total score - Part 2: {total_cards}")

# Someone has a serious gambling problem.





