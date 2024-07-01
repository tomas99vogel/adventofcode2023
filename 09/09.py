with open("input.txt", "r") as f:
    LINES = [line.strip() for line in f.readlines()] 


def extrapolate(array:list[list], reverse) -> int:
    if reverse:
        array[-1].insert(0,0)
        for i in range(len(array)-1,0,-1):
            array[i-1].insert(0,array[i-1][0]-array[i][0])
        return array[0][0]
    else:   
        array[-1].append(0)
        for i in range(len(array)-1,0,-1):
            array[i-1].append(array[i-1][-1]+array[i][-1])
        return array[0][-1]

def reduce_line(line:list) -> int:
    prediction_array = [line]
    current_line = line
    next_line = []

    is_all_zero = all(v == 0 for v in current_line)

    while not is_all_zero:
        next_line = []
        for i in range(len(current_line)-1):
            next_line.append(current_line[i+1] - current_line[i])
        prediction_array.append(next_line)
        current_line = next_line
        is_all_zero = all(v == 0 for v in current_line) 

    return extrapolate(prediction_array,reverse)

if __name__ == '__main__':
    result = 0
    reverse = False # Part 1 = False, Part 2 = True 

    for line in LINES:
        line = list(map(int,line.split(" ")))
        result += reduce_line(line)

