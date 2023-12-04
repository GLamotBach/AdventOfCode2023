# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 2 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

max_red = 12
max_green = 13
max_blue = 14
possible_games = []
total_power = 0

with open('day_2_input.txt', 'r') as input_file:
    for line in input_file:
        line = line.split(":")
        game = line[0].split()
        game = game[1]
        cubes = line[1]
        cubes = cubes.replace(";", ",")
        cubes = cubes.replace("\n", "")
        cubes = cubes.split(',')
        impossible_game = False
        red_cubes = []
        green_cubes = []
        blue_cubes = []
        for cube in cubes:
            cube = cube.split()
            if cube[1] == 'red':
                red_cubes.append(int(cube[0]))
                if int(cube[0]) > max_red:
                    impossible_game = True
            elif cube[1] == 'green':
                green_cubes.append(int(cube[0]))
                if int(cube[0]) > max_green:
                    impossible_game = True
            elif cube[1] == 'blue':
                blue_cubes.append(int(cube[0]))
                if int(cube[0]) > max_blue:
                    impossible_game = True

        line_power = max(red_cubes) * max(green_cubes) * max(blue_cubes)
        total_power += line_power
        if not impossible_game:
            possible_games.append(int(game))

print(f"Possible games: {sum(possible_games)}")
print(f"Total power: {total_power}")


