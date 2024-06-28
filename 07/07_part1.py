from functools import cmp_to_key


with open("input.txt") as f:
    LINES = [line.strip() for line in f.readlines()]

hands = {
    "single": [],
    "pair": [],
    "two_pairs": [],
    "three": [],
    "fullhouse": [],
    "four": [],
    "five": []
}

def convert_cards(cards:list) -> list:
    cards_conversion = {
    "A": 14, 
    "K": 13, 
    "Q": 12, 
    "J": 11, 
    "T": 10
    }
    converted_cards = []
    for card in cards:
        if card in cards_conversion:
            card = cards_conversion[card]
            converted_cards.append(card)
        else:
            converted_cards.append(card)
    return converted_cards

def score_hand(hand):
    combo = {}
    for card in hand:
        if card in combo:
            combo[card] += 1
        else:
            combo[card] = 1

    if len(combo) == 1:
        return "five"
    if len(combo) == 2:
        if 4 in combo.values():
            return "four"
        else:
            return "fullhouse"

    if len(combo) == 3:
        if 3 in combo.values():
            return "three"      
        else:
            return "two_pairs"

    if len(combo) == 4:
        return "pair"

    if len(combo) == 5:
        return "single"

def parse_hand(hand):
    cards = list(map(int,convert_cards(list(hand.split(" ")[0]))))
    hand = {
        "cards": cards,
        "bet": int(hand.split(" ")[1]),
        "combo": score_hand(cards),
        "value": 0
    }
    return hand

if __name__ == '__main__':
    part_one = 0
    for line in LINES:
        hand = parse_hand(line)
        hands[hand["combo"]].append(hand)
    
    order = 1
    for p in hands.keys():
        for hand in sorted(hands[p], key=lambda x: x['cards']):
            print(order, hand)
            part_one += order*hand["bet"]
            order += 1
        #hands[p] = merge_sort(hands[p]["cards"])


    print(part_one)
