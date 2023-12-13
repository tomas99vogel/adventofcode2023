import re

with open("input.txt", "r") as f:
    lines = f.readlines()
LINES = [line.strip() for line in lines] 

def get_symbols() -> set:
    symbols = []
    for line in LINES:
        for c in line:
            if not c.isalnum() and c not in (",. "):
                symbols.append(c)
    return set(symbols)

def seek_adjacent(line_num:int, coords:tuple, symbols:list) -> bool:
    adjacent_chars = []
    print(LINES[line_num][coords[0]:coords[1]])
    if line_num != 0: # previous line (can overflow)
        adjacent_chars.append(LINES[line_num-1][coords[0]-1:coords[1]+1])
    adjacent_chars.append(LINES[line_num][coords[0]-1:coords[0]+1]) # current line
    if line_num != 139: # last line (can overflow)
        adjacent_chars.append(LINES[line_num+1][coords[0]-1:coords[1]+1])

    adjacent_chars = [l for ls in adjacent_chars for l in ls]
    print(adjacent_chars)
    for c in set(adjacent_chars):
        if c in symbols: 
            return True
    return False

def part_one():
    symbols = get_symbols() # '-', '=', '+', '/', '#', '&', '%', '$', '@', '*'
    sum = 0

    for idx,line in enumerate(LINES):
        
        #numbers = {}
        matches = re.finditer(r'\b\d+\b', line)
        for match in matches:
            print(match)
            #numbers[match.group()] = match.span()
            if seek_adjacent(idx,match.span(),symbols):
                print(match.group())
                sum += int(match.group())
    return sum

symbols = get_symbols()
print(seek_adjacent(138,(107, 110),symbols))
#print(part_one())


#print(seek_adjacent(0,test["227"],symbols))
