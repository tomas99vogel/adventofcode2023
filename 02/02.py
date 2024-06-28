# Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

with open("input.txt") as f:
    LINES = f.readlines()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def parse_line(line) -> dict[str:list]:
    sets = {
        "red": [],
        "green": [],
        "blue": []
    }
    games = [game.strip() for game in line.split(": ")[1].split(";")]

    for s in games:
        cubes = s.split(", ")
        for color in sets.keys():
            for c in cubes:
                if color in c:
                    sets[color].append(int(c.split(" ")[0]))
    return sets

def check_game(game:dict) -> bool:
    if max(game["red"]) > MAX_RED:
        return False
    if max(game["green"]) > MAX_GREEN:
        return False
    if max(game["blue"]) > MAX_BLUE:
        return False 
    return True  

if __name__ == '__main__':
    part_1 = 0
    part_2 = 0
    for idx,line in enumerate(LINES):
        game = parse_line(line)

        # Part 1
        if check_game(game):
            part_1 += idx+1
        
        # Part 2
        power = 1
        for color in game:
            power *= max(game[color])

        part_2 += power

    print(part_1)
    print(part_2)
