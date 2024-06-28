
with open("input.txt", "r") as f:
    LINES = [line.strip() for line in f.readlines()] 

line_count = len(LINES)
line_width = len(LINES)

def get_symbols() -> set:
    symbols = set()
    for line in LINES:
        for c in line:
            if not c.isdigit() and c != ".":
                symbols.add(c)
    return symbols


def check_adjacent(line:int, position:int, num_len: int) -> bool:
    for x in range(line-1, line+2):
        for y in range(position-num_len-1, position+1):
            try:
                if LINES[x][y] in SYMBOLS:
                    return True
            except IndexError:
                continue
            
    return False

SYMBOLS = get_symbols()

if __name__ == '__main__':
    sum = 0
    number = ""

    for id_x, line in enumerate(LINES):
        for id_y, c in enumerate(line):
            if c.isdigit():
                number+=c
            else:
                if number:
                    if id_y == 0:
                        id_y = line_width
                    if check_adjacent(id_x,id_y,len(number)):
                        sum += int(number)
                else:
                    continue
                number = ""

    print(sum)