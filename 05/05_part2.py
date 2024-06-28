with open('input.txt') as f:
    f = f.read()

def parse_input(f):

    parts = f.split('\n\n')

    seeds = []
    seeds_ranges = [int(s) for s in parts[0].split(": ")[1].split(" ")]

    for i in range(0,len(seeds_ranges), 2):
        seeds.append([seed for seed in range(seeds_ranges[i], seeds_ranges[i]+seeds_ranges[i+1])])
    seeds = [int(seed) for seed_list in seeds for seed in seed_list]

    maps = []
    for map in parts[1:]:
        conversion_map = map.split('\n')[1:]
        conversion_map = [n for n in conversion_map]
        maps.append(conversion_map)
    return seeds, maps


def convertor(seed:int, maps:list) -> int:
    next_number = seed

    for map in maps:
        map = [int(i) for i in map.split(" ")]

        destination = map[0]
        source = map[1]
        range_lenght = map[2]
        if seed in range(source, source+range_lenght):
            next_number = seed + (destination-source) 

    return next_number


if __name__ == '__main__':
    seeds, maps = parse_input(f)
    locations = {}

    for seed in seeds:
        if seed in locations:
            continue
        else:
            next_number = seed
            for map in maps:
                next_number = convertor(next_number, map)
        locations[seed] = int(next_number)
    
    lowest_location = min(locations, key=locations.get)
    print(lowest_location)

