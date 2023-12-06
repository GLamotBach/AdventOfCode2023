# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *   *   *   *   Day 5 - Puzzle 1    *   *   *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

def import_map(file):
    with open(file, 'r') as import_file:
        imported_map = []
        for line in import_file:
            line = line.split()
            imported_line = []
            for number in line:
                number = int(number)
                imported_line.append(number)
            imported_map.append(imported_line)
        return imported_map

def map_navigator(origin, map_object):
    destination = origin
    for line in map_object:
        if line[1] <= origin <= (line[1] + line[2]):
            destination = line[0] + (origin - line[1])
    return destination


def map_navigator_navigator():
    seeds = import_map('day_5_seeds.txt')
    seeds = seeds[0]
    seed_to_soil = import_map('day_5_seed_to_soil.txt')
    soil_to_fertilizer = import_map('day_5_soil_to_fertilizer.txt')
    fertilizer_to_water = import_map('day_5_fertilizer_to_water.txt')
    water_to_light = import_map('day_5_water_to_light.txt')
    light_to_temperature = import_map('day_5_light_to_temperature.txt')
    temperature_to_humidity = import_map('day_5_temperature_to_humidity.txt')
    humidity_to_location = import_map('day_5_humidity_to_location.txt')
    locations = []
    for seed in seeds:
        a = map_navigator(seed, seed_to_soil)
        b = map_navigator(a, soil_to_fertilizer)
        c = map_navigator(b, fertilizer_to_water)
        d = map_navigator(c, water_to_light)
        e = map_navigator(d, light_to_temperature)
        f = map_navigator(e, temperature_to_humidity)
        g = map_navigator(f, humidity_to_location)
        locations.append(g)

    return locations


def the_thing_doer(say_it):
    """Does the thing"""
    if say_it == 'Do da thing!':
        locations = map_navigator_navigator()
        shortest = min(locations)
        print(f"Part 1: {shortest}")
    else:
        print('Say it!')


the_thing_doer('Do da thing!')

# Part - 2

def location_map_sorter():
    location_map = import_map('day_5_humidity_to_location.txt')
    #sorted(location_map, key=lambda x: x[0])
    location_map.sort()
    for line in location_map:

        print(line)
        print(line[0] + line[2])

# For simplicity the range of locations is from 0 to 4294967296

def reverse_map_navigator(destination, map_object):
    origin = destination
    for line in map_object:
        if line[0] <= destination <= (line[0] + line[2]):
            origin = line[1] + (destination - line[0])
    return origin

def format_seed():
    seeds = import_map('day_5_seeds.txt')
    seeds = seeds[0]
    formated_seeds = []
    for seed in range(0, len(seeds), 2):
        line =[]
        line.append(seeds[seed])
        line.append(seeds[seed + 1])
        formated_seeds.append(line)
    return formated_seeds


def reverse_map_navigator_navigator():
    seed_to_soil = import_map('day_5_seed_to_soil.txt')
    soil_to_fertilizer = import_map('day_5_soil_to_fertilizer.txt')
    fertilizer_to_water = import_map('day_5_fertilizer_to_water.txt')
    water_to_light = import_map('day_5_water_to_light.txt')
    light_to_temperature = import_map('day_5_light_to_temperature.txt')
    temperature_to_humidity = import_map('day_5_temperature_to_humidity.txt')
    humidity_to_location = import_map('day_5_humidity_to_location.txt')
    seeds = format_seed()
    for location in range(4294967296):
        g = reverse_map_navigator(location, humidity_to_location)
        f = reverse_map_navigator(g, temperature_to_humidity)
        e = reverse_map_navigator(f, light_to_temperature)
        d = reverse_map_navigator(e, water_to_light)
        c = reverse_map_navigator(d, fertilizer_to_water)
        b = reverse_map_navigator(c, soil_to_fertilizer)
        a = reverse_map_navigator(b, seed_to_soil)
        for seed in seeds:
            if seed[0] <= a <= (seed[0] + seed[1]):
                return location


print(f"Part 2: {reverse_map_navigator_navigator()}")




