import random

deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A" ]
player = []
dealer = []

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
            total +=1
        else:
            if total >11:
                total += 1
            else:
                total = 11
    return total

def revealdealer():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) >2:
        return dealerhand[0], dealerhand[1]