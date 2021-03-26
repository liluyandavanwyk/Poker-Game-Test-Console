import itertools
import random
import hands

CARD_PRINT = 'Card {}: {:<5} of {}'

OPENING_MESSAGE = 'Welcome to Console Poker Test!'
HAND_MESSAGE = 'Your hand:'

SWAP_MESSAGE = 'Which cards would you like to swap out?'
SWAP_HELP = 'Type in the numbers of the cards (1-5), separated by a space.\n' \
               'For example: "1 3 4" would swap out card #1, #3 and #4.\n' \
               'If you would like to keep all your cards, type "0".'
INPUT_ERROR = 'Invalid input!'

SWAP_NONE = 'No cards will be swapped!'
SWAP_EXIST = 'The following card(s) were swapped:'
SWAP_DATA = '{:<5} of {}'
SWAP_NEW = 'Your new hand:'

HAND_RESULT = 'Congratulations! You have: {}!'

PROMPT_ROUND = 'Would you like to play another round? (Y/N) '
NEW_ROUND = 'Starting a new round!'

END_GAME = 'Thanks for playing!'

flag_help = True

SUITS = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
NUMBERS = hands.NUMBERS
cards = list(itertools.product(NUMBERS, SUITS))
hand = []
used = []


def poker_game():
    poker_start()
    poker_loop()


def poker_start():
    print(OPENING_MESSAGE)
    print()


def poker_loop():
    while True:
        generate_hand()
        swap_hand()
        identify_hand()
        clear_hand()
        check_round()


def generate_hand():
    random.shuffle(cards)
    for i in range(5):
        if len(cards) > 0:
            hand.append(cards.pop())
        else:
            reset_cards()
            hand.append(cards.pop())

    print(HAND_MESSAGE)
    print_hand()


def swap_hand():
    print(SWAP_MESSAGE)
    global flag_help
    if flag_help:
        print(SWAP_HELP)
        flag_help = False

    while True:
        indexes = set()
        try:
            command = input()
            print()
            swap = command.split()
            for i in swap:
                index = int(i)

                if index < 0 or index > 5:
                    raise ValueError

                indexes.add(index)

            if 0 in indexes:
                print(SWAP_NONE)
                break
            else:
                print(SWAP_EXIST)
                for i in indexes:
                    print(CARD_PRINT.format(i, hand[i - 1][0], hand[i - 1][1]))

                    if len(cards) > 0:
                        used.append(hand[i - 1])
                        hand[i - 1] = cards.pop()
                    else:
                        reset_cards()
                        used.append(hand[i - 1])
                        hand[i - 1] = cards.pop()
                print()

                print(SWAP_NEW)
                print_hand()
                break

        except ValueError:
            print(INPUT_ERROR)
            print(SWAP_HELP)
            continue


def identify_hand():
    result = hands.find_hands(hand)
    print(HAND_RESULT.format(result))
    print()


def clear_hand():
    for card in hand:
        used.append(card)

    hand.clear()


def check_round():
    while True:
        ans = input(PROMPT_ROUND)

        if ans == 'Y' or ans == 'y':
            print(NEW_ROUND)
            print()
            break
        elif ans == 'N' or ans == 'n':
            print(END_GAME)
            exit(-1)
        else:
            print(INPUT_ERROR)


def reset_cards():
    cards.extend(used)
    used.clear()


def print_hand():
    i = 1
    for card in hand:
        print(CARD_PRINT.format(i, card[0], card[1]))
        i = i + 1

    print()


if __name__ == '__main__':
    poker_game()
