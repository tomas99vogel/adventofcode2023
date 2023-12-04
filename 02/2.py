# Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

import re

CUBE_BAG = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_line(line:str) -> bool:
    valid_game = True

    cube_count = {
        "red": [],
        "green": [],
        "blue": []
    }
    
    games = line.split(":")[1].split(";")

    for game in games:
        cubes = game.split(",")
        #print(cubes )
        for cube in cubes:
            if "red" in cube:
                cube_count["red"] += (re.findall(r'[0-9]+',cube))
            if "green" in cube:
                cube_count["green"] += (re.findall(r'[0-9]+',cube))
            if "blue" in cube:
                cube_count["blue"] += (re.findall(r'[0-9]+',cube))

    for key,value in cube_count.items():
        print(cube_count[key])
        cube_count[key] = (min([eval(i) for i in value]))
        cube_count[key] = (max([eval(i) for i in value]))
        
        if cube_count[key][1] > CUBE_BAG[key]:
            return False
    return valid_game

    #print(games)

    #numbers = re.findall(r'\d.', "".join(games))
    #print(numbers)
    #if max(numbers) < 12:
    #    return True


with open("input.txt", "r") as f:
    lines = f.readlines()

    valid_id_sum = 0
    for idx,line in enumerate(lines):
        line = line.strip()
        if parse_line(line):
            valid_id_sum += idx+1
    print(valid_id_sum)

