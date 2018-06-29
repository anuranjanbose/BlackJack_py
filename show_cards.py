def show_some(player,dealer):

    print("\nDEALER HAND:")
    print("1 card is hidden!")
    print(dealer.cards[1])
    print("\n")
    print("PLAYER HAND:")
    for card in player.cards:
        print(card)

def show(player,dealer):
    print("\nDEALER HAND:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("PLAYER HAND:")
    for card in player.cards:
        print(card)