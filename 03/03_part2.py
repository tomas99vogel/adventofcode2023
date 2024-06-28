
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



def check_adjacent(line:int, position:int, num_len: int) -> tuple:
    for x in range(line-1, line+2):
        for y in range(position-num_len-1, position+1):
            if x in range(0,line_count) and y in range(0,line_width) :
                if LINES[x][y] == "*":
                    return (x,y)
            else:
                continue
            
    return None

SYMBOLS = get_symbols()

if __name__ == '__main__':
    sum = 0
    number = ""
    count =0
    num_to_symbols = {}

    for id_x, line in enumerate(LINES):
        for id_y, c in enumerate(line):
            if c.isdigit():
                number+=c
            else:
                if number:
                    if id_y == 0:
                        id_y = line_width
                    asterisk_coords = check_adjacent(id_x,id_y,len(number))
                    if asterisk_coords:
                        try: 
                            num_to_symbols[asterisk_coords].append(number)
                        except KeyError:
                            num_to_symbols[asterisk_coords] = [] 
                            num_to_symbols[asterisk_coords].append(number)                     
                else:
                    continue
                number = ""
    for nums in num_to_symbols.values():
        gear = 1
        
        if len(nums) == 2:
            for i in nums:
                gear *= int(i)
            sum += gear
    print(sum)