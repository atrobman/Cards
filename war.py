from card import Card, Suit, CardValue
from random import shuffle

def printLineOfCards(cards_to_print : list[Card], spaces : int = 2, spaces_char : str = " ") -> None :
    '''
    Print a list of Cards on a single line
    '''

    if len(cards_to_print) == 0:
        return

    str_converted = [card.getCardStr() for card in cards_to_print]
    spaces_str = spaces_char * spaces
    print("".join(spaces_str.join(card[line] for card in str_converted) + "\n" for line in range(len(str_converted[0]))))

deck = []
NUM_DECKS = 1
for value in CardValue:
    for suit in Suit:
        for _ in range(NUM_DECKS):
            deck.append(Card(suit, value))

shuffle(deck)

player_hands = [[deck.pop() for _ in range(NUM_DECKS * 26)] for _ in range(2)]
STEP_BY_STEP = True

while len(player_hands[0]) > 0 and len(player_hands[1]) > 0:
    p1_card = player_hands[0].pop()
    p2_card = player_hands[1].pop()

    print("-----------------------------------------------------\n")
    print("           #           ")
    print("PLAYER  1  #  PLAYER  2")
    printLineOfCards((p1_card, p2_card), spaces=1, spaces_char="  #  ")

    if p1_card > p2_card:
        print("# PLAYER 1 WINS #")
        player_hands[0] += (p1_card, p2_card)
    elif p2_card > p1_card:
        print("# PLAYER 2 WINS #")
        player_hands[1] += (p1_card, p2_card)
    else:
        print("#      TIE      #")
        tie_broken = False
        revealed_cards = [[p1_card], [p2_card]]
        while not tie_broken and len(player_hands[0]) > 0 and len(player_hands[1]) > 0:
            if STEP_BY_STEP:
                input(" - press ENTER to do tiebreaker - ")

            display_p1 = []
            display_p2 = []

            reveal_num_p1 = min(3, len(player_hands[0]) - 1)
            reveal_num_p2 = min(3, len(player_hands[1]) - 1)

            if reveal_num_p1 != 3 or reveal_num_p2 != 3:
                if STEP_BY_STEP:
                    input(" - press ENTER to continue - ")

            for _ in range(reveal_num_p1):
                display_p1.append(player_hands[0].pop())
            for _ in range(reveal_num_p2):
                display_p2.append(player_hands[1].pop())

            final_card_p1 = player_hands[0].pop()
            final_card_p2 = player_hands[1].pop()

            for card in display_p1:
                card.hidden = True
            for card in display_p2:
                card.hidden = True

            printLineOfCards(display_p1)
            printLineOfCards((final_card_p1,))
            print('\n')
            printLineOfCards(display_p2)
            printLineOfCards((final_card_p2,))

            for card in display_p1:
                card.hidden = False
            for card in display_p2:
                card.hidden = False

            revealed_cards[0] += display_p1
            revealed_cards[1] += display_p2
            revealed_cards[0].append(final_card_p1)
            revealed_cards[1].append(final_card_p2)
            
            if final_card_p1 > final_card_p2:
                print("# PLAYER 1 WINS #")
                player_hands[0] += revealed_cards[0]
                player_hands[0] += revealed_cards[1]
                tie_broken = True

            elif final_card_p2 > final_card_p1:
                print("# PLAYER 2 WINS #")
                player_hands[1] += revealed_cards[0]
                player_hands[1] += revealed_cards[1]
                tie_broken = True

            elif len(player_hands[0]) == 0:
                print("# TIE FAILED, PLAYER 1 RAN OUT OF CARDS #")
                player_hands[0] += revealed_cards[0]
                player_hands[1] += revealed_cards[1]
                tie_broken = True

            elif len(player_hands[1]) == 0:
                print("# TIE FAILED, PLAYER 2 RAN OUT OF CARDS #")
                player_hands[0] += revealed_cards[0]
                player_hands[1] += revealed_cards[1]
                tie_broken = True

        if not tie_broken:
            if len(player_hands[0]) == 0:
                print("# TIE FAILED, PLAYER 1 RAN OUT OF CARDS #")
            else:
                print("# TIE FAILED, PLAYER 2 RAN OUT OF CARDS #")

            player_hands[0] += revealed_cards[0]
            player_hands[1] += revealed_cards[1]

    shuffle(player_hands[0])
    shuffle(player_hands[1])
    print("CARDS LEFT: ")
    print(f"PLAYER 1 - {len(player_hands[0])}")
    print(f"PLAYER 2 - {len(player_hands[1])}")
    print("-----------------------------------------------------")

    if STEP_BY_STEP:
        input(" - press ENTER to continue - ")

if len(player_hands[0]) == 0:
    print("# PLAYER 2 WINS #")
elif len(player_hands[1]) == 0:
    print("# PLAYER 1 WINS #")