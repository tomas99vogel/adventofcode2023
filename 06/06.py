with open("input.txt", "r") as f:
    lines = [line.strip().split() for line in f.readlines()]

races = []
for i in range(1,len(lines[0])):
    races.append((lines[0][i],lines[1][i]))

def part_one():
    result = 1
    for race in races:
        variations = 0

        max_time = int(race[0])
        max_distance = int(race[1])

        for speed in range(1,max_time): # hold time == speed - from 1 to max time
            time_remaining = max_time - speed
            distance = speed * time_remaining
            if distance > max_distance:
                variations += 1
        result *= variations
    return result

# part two
def part_two():
    final_race = (49877895,356137815021882)
    variations = 0
    for speed in range(1,final_race[0]):
                time_remaining = final_race[0] - speed
                distance = speed * time_remaining
                if distance > final_race[1]:
                    variations += 1
    return variations

print(part_one())
