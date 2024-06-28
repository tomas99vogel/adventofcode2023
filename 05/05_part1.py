with open('input_test.txt') as f:
    f = f.read()

def parse_input(f):

    parts = f.split('\n\n')
    seeds = [int(s) for s in parts[0].split(": ")[1].split(" ")]

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
    
    locations = []
    for seed in seeds:
        next_number = seed
        for map in maps:
            next_number = convertor(next_number, map)
        locations.append(int(next_number))
    
    lowest_location = min(locations)
    print(lowest_location)
