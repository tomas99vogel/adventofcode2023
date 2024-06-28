
with open("input.txt") as f:
    LINES = f.readlines()

def parse_hand(line):
    card = {}
    line = line.replace("  ", " ")
    winning_numbers, my_numbers = line.split(" | ")
    
    card_number, winning_numbers = winning_numbers.split(": ")

    card_number = card_number.split(" ")[-1]
    winning_numbers = [int(i) for i in winning_numbers.split(" ")]
    my_numbers = [int(i) for i in my_numbers.split(" ")]
    
    value = 0
    for i in my_numbers:
        if i in winning_numbers:
            if value == 0:
                value = 1
            else:
                value *= 2

    return value
    return sum(1 for i in my_numbers if i in winning_numbers)


if __name__ == '__main__':
    total = 0


    for line in LINES:
        total += parse_hand(line)
    
    print(total)

