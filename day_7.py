# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 7 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *


card_value = {
    'A': '14', 'K': '13', 'Q': '12', 'J': '11', 'T': '10', '9': '09', '8': '08', '7': '07', '6': '06', '5': '05',
    '4': '04', '3': '03', '2': '02',
}

all_hands = []
with open('day_7_input.txt', 'r') as import_file:
    for line in import_file:
        line = line.split()
        line[1] = int(line[1])
        all_hands.append(line)

for hand in all_hands:
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    highest_count = 0
    second_count = 0
    hand.append("")
    for card in cards:
        a = hand[0].count(card)
        if a > highest_count:
            second_count, highest_count = highest_count, a
        elif a > second_count:
            second_count = a
    if highest_count == 5:
        hand[2] = hand[2] + '7'
    elif highest_count == 4:
        hand[2] = hand[2] + '6'
    elif highest_count == 3 and second_count == 2:
        hand[2] = hand[2] + '5'
    elif highest_count == 3:
        hand[2] = hand[2] + '4'
    elif highest_count == 2 and second_count == 2:
        hand[2] = hand[2] + '3'
    elif highest_count == 2:
        hand[2] = hand[2] + '2'
    else:
        hand[2] = hand[2] + '1'

    for card in hand[0]:
        hand[2] = hand[2] + card_value[card]

all_hands.sort(key=lambda x: x[2])

score = 0
for i in range(len(all_hands)):
    score += (i + 1) * int(all_hands[i][1])

print(f"Total score is: {score}")

#   *   *   *   *   *   *   *   *   *   *   *   *   Day 7 - Puzzle 2    *   *   *   *   *   *   *   *   *   *   *   *

# Let's reuse the code from Puzzle 1 with some modifications.

# Assign value '01' to jocker
card_value = {
    'A': '14', 'K': '13', 'Q': '12', 'J': '01', 'T': '10', '9': '09', '8': '08', '7': '07', '6': '06', '5': '05',
    '4': '04', '3': '03', '2': '02',
}

all_hands = []
with open('day_7_input.txt', 'r') as import_file:
    for line in import_file:
        line = line.split()
        line[1] = int(line[1])
        all_hands.append(line)

for hand in all_hands:
    # Remove jocker from list of cards to check
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    highest_count = 0
    second_count = 0
    hand.append("")
    # Count the jockers in hand
    jocker_count = hand[0].count('J')
    for card in cards:
        a = hand[0].count(card)
        if a > highest_count:
            second_count, highest_count = highest_count, a
        elif a > second_count:
            second_count = a
    # And add the jocker count to the highest count.
    highest_count = highest_count + jocker_count
    if highest_count == 5:
        hand[2] = hand[2] + '7'
    elif highest_count == 4:
        hand[2] = hand[2] + '6'
    elif highest_count == 3 and second_count == 2:
        hand[2] = hand[2] + '5'
    elif highest_count == 3:
        hand[2] = hand[2] + '4'
    elif highest_count == 2 and second_count == 2:
        hand[2] = hand[2] + '3'
    elif highest_count == 2:
        hand[2] = hand[2] + '2'
    else:
        hand[2] = hand[2] + '1'

    for card in hand[0]:
        hand[2] = hand[2] + card_value[card]

all_hands.sort(key=lambda x: x[2])

score = 0
for i in range(len(all_hands)):
    score += (i + 1) * int(all_hands[i][1])

# And bam !
print(f"Total score with jokers is: {score}")

