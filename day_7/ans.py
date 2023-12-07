file = "input.txt"
dummy1 = "dummy1.txt"

# five_of_a_kind = 6
# four of a kind = 5
# full house = 4
# three of a kind = 3
# two of a kind = 2
# one pair = 1
# high card = 0

def determine_hand(hand: str) -> int:
    if len(set(hand)) == 5:
        return 0
    if len(set(hand)) == 1:
        return 6
    if len(set(hand)) == 2:
        count = hand.count(hand[0])
        return 5 if count == 1 or count == 4 else 4
    if len(set(hand)) == 3:
        for i in hand:
            if hand.count(i) == 3:
                return 3
        return 2
    return 1

# five_of_a_kind = 6
# four of a kind = 5
# full house = 4
# three of a kind = 3
# two of a kind = 2
# one pair = 1
# high card = 0

def determine_hand_part_2(hand: str) -> int:
    jokerless_hand = hand.replace("J", "")
    joker_count = hand.count("J")
    num_unique_cards = len(set(jokerless_hand))
    if num_unique_cards == 0:
        return 6
    if num_unique_cards == 1:
        return 6
    if num_unique_cards == 2:
        if joker_count == 3:
            return 5
        if joker_count == 2:
            return 5
        if joker_count == 1:
            some_count = hand.count(jokerless_hand[0])
            if some_count == 2:
                return 4
            return 5
        count = hand.count(hand[0])
        return 5 if count == 1 or count == 4 else 4
    if num_unique_cards == 3:
        if (joker_count == 0):
            for i in hand:
                if hand.count(i) == 3:
                    return 3
            return 2
        return 3
    if num_unique_cards == 4:
        return 1
    return 0

def part1(file: str) -> int:
    ans = 0
    hand_to_bet = {}
    hands_ordered = []
    ranks = {"A": 13, "K" : 12, "Q": 11, "J" : 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            hand, bet = line.split()
            hand_to_bet[hand] = int(bet)
            power = determine_hand(hand)
            index = 0
            for i, played_hand in enumerate(hands_ordered):
                if played_hand[1] > power:
                    break
                if played_hand[1] == power:
                    worse_hand = True
                    for i in range(5):
                        cur_card = hand[i]
                        other_card = played_hand[0][i]
                        if ranks[cur_card] < ranks[other_card]:
                            worse_hand = True
                            break
                        if ranks[cur_card] > ranks[other_card]:
                            worse_hand = False
                            break
                    if (worse_hand):
                        break

                index += 1
            hands_ordered.insert(index, (hand, power))
            
    for i, hand in enumerate(hands_ordered):
        ans += (i + 1) * hand_to_bet[hand[0]]
    return ans

def part2(file: str) -> int:
    ans = 0
    hand_to_bet = {}
    hands_ordered = []
    ranks = {"A": 13, "K" : 12, "Q": 11, "J" : 0, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            hand, bet = line.split()
            hand_to_bet[hand] = int(bet)
            power = determine_hand_part_2(hand)
            index = 0
            for i, played_hand in enumerate(hands_ordered):
                if played_hand[1] > power:
                    break
                if played_hand[1] == power:
                    worse_hand = True
                    for i in range(5):
                        cur_card = hand[i]
                        other_card = played_hand[0][i]
                        if ranks[cur_card] < ranks[other_card]:
                            worse_hand = True
                            break
                        if ranks[cur_card] > ranks[other_card]:
                            worse_hand = False
                            break
                    if (worse_hand):
                        break

                index += 1
            hands_ordered.insert(index, (hand, power))
            
    for i, hand in enumerate(hands_ordered):
        ans += (i + 1) * hand_to_bet[hand[0]]
    return ans

ans1 = part1(file)
print(f"part1: {ans1}")
ans2 = part2(file)
print(f"part2: {ans2}")