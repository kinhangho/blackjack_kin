import random
from termios import FF1

playerIn = True
dealerIn = True

deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A" ]
player = []
dealer = []

class Cards:
    def dealcard(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)


    def total(turn):
        total = 0
        face = ["K", "Q", "j"]
        for card in turn:
            if card in range(1,11):
                total += card
            elif card in face:
                total += 10
            else:
                if total >11:
                    total += 1
                else:
                    total = 11
        return total

class Dealing:
    def revealdealer():
        if len(dealer) == 2:
            return dealer[0]
        elif len(dealer) >2:
            return dealer[0], dealer[1]

    for _ in range(2):
        dealcard(dealer)
        dealcard(player)
        
        

    while dealerIn or playerIn:
        print(f"Dealer had {revealdealer()}and X")
        print(f"You have {player} for a total of {total(player)}")
        if playerIn:
            stayOrhit = input("1:Stay\n 2:Hit\n")
        if total(dealer) >16:
            dealerIn = False
        else:
            dealcard(dealer)
        if stayOrhit =='1':
            playerIn = False
        else:
            dealcard(player)
        if total(player) >= 21:
            break
        if total(dealer) >= 21:
            break

    if total(player) == 21:
        print(f"\nYou have {player} for a total of {total(player)} and dealer has {total(dealer)}")
        print("Blackjack! You are the winner")
    elif total(dealer) == 21:
        print(F"Good bye!!! Dealer has {total(dealer)}, Blackjack")
    elif total(player) > 21:
        print(f"You lose, You have {total(player)} bust")
    elif total(dealer) > 21:
        print(f"You win, You have {total(player)} and dealer bust")
    elif 21 - total(dealer) < 21 - total(player):
        print(f"\nYou have {player} for a total of {total(player)} and dealer has {total(dealer)}")
        print("Dealer wins!!")
    elif 21 - total(dealer) > 21 - total(player):
        print(f"\nYou have {player} for a total of {total(player)} and dealer has {total(dealer)}")
        print("You wins!!")