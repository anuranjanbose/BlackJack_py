def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("Enter your bet amount: "))
        except:
            print("Enter a number for amount!")
            continue
        else:
            if chips.bet > chips.total :
                print("Insufficient balance. You have {} chips".format(chips.total))
            else:
                break


def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_aces()


def hit_or_stand(deck,hand):

    #global playable

    while True:
        x = input("Hit OR Stand?..(h/s)").lower()

        if x[0] == 'h':
            hit(deck,hand)
            return True
        elif x[0] == 's':
            print("Player's Turn Over")
            print("Dealer's Turn Now")
            return False
        else:
            print("Didnt understand that, please enter again")
            continue
        break





def player_wins(player,dealer,chips):
    print("PLAYER WINS")
    chips.win_bet()

def player_busts(player,dealer,chips):
    print("PLAYER BUSTS")
    chips.lose_bet()

def dealer_busts(player,dealer,chips):
    print("DEALER BUSTS")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS")
    chips.lose_bet()

def push(player,dealer):
    print("PLAYER & DEALER TIE!")


