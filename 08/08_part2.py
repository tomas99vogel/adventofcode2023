from sympy import factorint

with open("input.txt", "r") as f:
    instructions = f.readline().strip()
    
    nodes = {}
    for line in f.readlines()[1::]:
        line = line.strip().split(" = ")
        nodes[line[0]] = (line[1].strip("()").split(", "))

if __name__ == '__main__':

    starting_nodes = {node: [] for node in nodes.keys() if node[-1] == 'A'}
    for startpoint in starting_nodes:
        steps = 0
        node = startpoint
        while node[-1] != 'Z':         
            index = steps % len(instructions)
            
            if instructions[index] == "L":
                node = nodes[node][0]
            else:
                node = nodes[node][1]
            steps += 1
        else:
            starting_nodes[startpoint]= steps

    # least common multiple
    unique_primes = {}
    lcm = 1
    for n in starting_nodes.values():
        for prime, power in factorint(n).items():
            if prime not in unique_primes.keys():
                print(prime,power)
                unique_primes[prime] = power
                lcm *= pow(prime,power)
            else:
                continue
    print(lcm)


    #{'JHA': [('TBZ', 21883)], 'NCA': [('LQZ', 13019)], 'MMA': [('QDZ', 19667)], 'AAA': [('ZZZ', 16343)], 'TVA': [('FNZ', 18559)], 'DTA': [('FQZ', 14681)]}