
NUMBERS = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
ROYAL_FLUSH = ['ACE', 'KING', 'QUEEN', 'JACK', 'TEN']

HAND_ORDER = ['STRAIGHT FLUSH', 'FOUR OF A KIND', 'FULL HOUSE', 'FLUSH', 'STRAIGHT', 'THREE OF A KIND', 'TWO PAIR', 'ONE PAIR', 'HIGH CARDS', 'ROYAL FLUSH']

def royal_flush(hand):
    royal_flush = list(ROYAL_FLUSH)
    suit = hand[0][1]

    for card in hand:
        if card[1] is not suit:
            return False

        if card[0] not in royal_flush:
            return False

        royal_flush.remove(card[0])

    return True


def straight_flush(hand):
    return straight(hand) and flush(hand)


def straight(hand):
    numbers = sorted(hand, key=lambda card: card[0])
    if (NUMBERS.index(numbers[4][0]) - NUMBERS.index(numbers[0][0])) == 4:
        return True
    elif numbers[4] == 'ACE' and numbers[0] == 'TEN':
        return True


def flush(hand):
    suit = hand[0][1]

    for card in hand:
        if card[1] is not suit:
            return False

    return True


def find_hands(hand: list):
    counts = dict()

    for card in hand:
        if card[0] not in counts:
            counts[card[0]] = 1
        else:
            counts[card[0]] = counts[card[0]] + 1

    if len(counts) == 5:
        if royal_flush(hand):
            return HAND_ORDER[9]
        elif straight_flush(hand):
            return HAND_ORDER[8]
        elif flush(hand):
            return HAND_ORDER[5]
        elif straight(hand):
            return HAND_ORDER[4]
        else:
            return HAND_ORDER[0]

    elif len(counts) == 4:
        return HAND_ORDER[1]

    elif len(counts) == 3:
        if 3 in list(counts.values()):
            return HAND_ORDER[3]
        else:
            return HAND_ORDER[2]

    elif len(counts) == 2:
        if 3 in list(counts.values()):
            return HAND_ORDER[6]
        else:
            return HAND_ORDER[7]

