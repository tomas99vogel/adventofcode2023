with open("input_test.txt", "r") as f:
    LINES = [line.strip() for line in f.readlines()] 

def predict_next(line:list) -> int:
    current_line = line
    next_line = []

    sum = sum(current_line) 

    while sum:
        for i in range(len(line)):
            next_line[i] = current_line[i+1] - current_line[i]
            

for line in LINES:
    line = list(map(int,line.split(" ")))
    print(line)