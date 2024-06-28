with open("input.txt", "r") as f:
    instructions = f.readline().strip()
    
    nodes = {}
    for line in f.readlines()[1::]:
        line = line.strip().split(" = ")
        nodes[line[0]] = (line[1].strip("()").split(", "))

if __name__ == '__main__':
    steps = 0

    current_node = "AAA"
    while current_node != "ZZZ":
        index = steps % len(instructions)
        if instructions[index] == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        print(current_node, steps)

        steps += 1
    print(steps)

        
