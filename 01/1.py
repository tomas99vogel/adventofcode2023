import re

DIGITS = {
    'one' : '1',
    'two' : '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

sum = 0

def sort_list(input_list):
    sorted_list = sorted(input_list, key=lambda x: x[1])
    return sorted_list

# Try to translate the words into strings. If found, return first and last, along with their indexes
def seek_str_digits(line:list) -> list:
    matches = []

    for digit in DIGITS.keys():
       if digit in line:
           for m in re.finditer(digit, line):
                matches.append((DIGITS[digit], m.start()))
           
    return sort_list(matches)
           
# line with just basic digits. If found, return first and last, along with their indexes
def seek_digits(line:list) -> list:
    matches = re.findall(r'\d{1}', line)
    if matches:
        first_index = line.find(matches[0])
        if len(matches) > 1:

            last_index = line.rfind(matches[-1])

            return sort_list(((matches[0],first_index), (matches[-1],last_index)))
        else:
            return [(matches[0],first_index)]
    else:
        return []

with open("input.txt", "r") as f:
    input = f.readlines()
    for line in input:
        line = line.strip()

        num_matches = seek_digits(line)
        str_matches = seek_str_digits(line)

        # combine results and sort it by indexes
        merged_matches = num_matches + str_matches
        sorted_matches = sort_list(merged_matches)

        # only one number - edge case fix
        if len(sorted_matches) == 1:
            sum+=int("".join((sorted_matches[0][0]*2)))
            continue

        line_sum = int("".join(sorted_matches[0][0] + sorted_matches[-1][0]))
        sum+= int("".join(sorted_matches[0][0] + sorted_matches[-1][0]))

print(sum)

