
with open("input.txt") as f:
    LINES = f.readlines()

def parse_lines(LINES) -> dict:
    cards = {}

    for card in LINES:
        card = card.replace("  ", " ")
        winning_numbers, my_numbers = card.split(" | ")
        
        card_number, winning_numbers = winning_numbers.split(": ")

        card_number = int(card_number.split(" ")[-1])
        winning_numbers = [int(i) for i in winning_numbers.split(" ")]
        my_numbers = [int(i) for i in my_numbers.split(" ")]
        
        matches = sum(1 for i in my_numbers if i in winning_numbers)

        cards[card_number] = {
            "matches": matches,
            "count" : 1
        }

    return cards

if __name__ == '__main__':
    count = 0
    cards = parse_lines(LINES)

    max_idx = max(cards.keys())  

    for idx, card in cards.items():
        matches = card["matches"]
        for i in range(matches):
            next_idx = idx + i + 1
            if next_idx in cards: 
                cards[next_idx]["count"] += card["count"]
        count += card["count"]

    print(count)

