import  random
import os

from show_cards import show_some, show



from functions import take_bet,hit,hit_or_stand,player_wins,player_busts,dealer_wins,dealer_busts,push

#GLOBAL VARIABLES

suits = ['Hearts','Spades','Clubs','Diamonds']

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Jack','Queen','King','Ace')

values = { 'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'King':10,'Queen':10,'Jack':10,'Ace':11}

playable = True


#CLASSES

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.rank + " of " + card.suit
        print("Deck composition: ")
        return  deck_comp


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card





class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += 2*self.bet

    def lose_bet(self):
        self.total -= self.bet


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_aces(self):

        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



#Functions



#GAME STARTS HERE


#Set chips

player_chips = Chips()

while True:
    #WELCOME

    print("\t\t!!__WELCOME TO BLACKJACK GAME__!!\n\n")

    #GAME SETUP

    deck = Deck()

    deck.shuffle()

    #Setup players

    player_hand = Hand()

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    dealer_hand = Hand()

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())



    #Ask for Bet

    take_bet(player_chips)

    #Show some cards

    show_some(player_hand,dealer_hand)

    while playable:


        #Prompt player to Hit or Stand

        playable = hit_or_stand(deck,player_hand)

        #show some cards

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break


    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        #show all cards
        show(player_hand,dealer_hand)

        #Winning scenarios

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)



    print("\nPlayer you have {} chips available".format(player_chips.total))

    #Ask to play again

    ask = input("Want to play again? y/n").lower()

    if ask[0] == 'y':
        print("OK! Get ready for next round!")
        playable = True
    else:
        print("Thank You for playing!")
        break






