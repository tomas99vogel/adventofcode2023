with open("input.txt") as f:
    pipes = [pipe.strip() for pipe in f.readlines()]

starting_point = (0,0)
for x in range(len(pipes)):
    for y in range(len(pipes[0])):
        if pipes[x][y] == "S":
            starting_point = (x,y)
            break

up = (-1,0)
down = (1,0)
left = (0,-1)
right = (0,1)

pipe_types = {
    "|" : {down : down, up : up},
    "F": {up: right, left : down},
    "-" : {right : right, left : left},
    "L": {left : up, down : right},
    "J" : {right : up, down : left},
    "7" : {right : down, up : left}
}

def get_next_position(position:tuple[int,int],direction:tuple[int,int]):
    try:
        next_position:tuple = (position[0]+direction[0], position[1]+direction[1])
        next_pipe:str = pipes[next_position[0]][next_position[1]]

        if next_pipe == ".":
            return None

        try:
            next_direction = pipe_types[next_pipe][direction]
        except:
            return None
        return (next_position, next_direction)

    except IndexError:
        return None


def move(position, direction):
    steps = 1
    position, direction = get_next_position(position,direction)
    while position and position != starting_point:
        steps += 1
        try:
            position, direction = get_next_position(position, direction)
        except:
            return steps


print(starting_point)
print(move(starting_point,right)//2)