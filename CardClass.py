# File       : Card Class
# Author     : Mir Ahmed
#Description : The following program creates a two classes called Card and Deck
#              and runs a simulation to determine cards matching during each random
#              dealing of cards from two decks.
#Date-created: 10/30/2010

import random

class Card:
    def __init__(self, f, s):
        self.myFaceValue = f
        self.mySuit = s
    def __str__(self):
        return self.myFaceValue + " of " + self.mySuit
    def getFaceValue(self):
        return self.myFaceValue
    def getSuit(self):
        return self.mySuit

class Deck:
    facevalues = ['Ace', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    def __init__(self):
        self.deckOfCards_ = [Card(faceValue, suit)
                             for faceValue in Deck.facevalues
                             for suit in Deck.suits]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.deckOfCards_)
    def dealCard(self):
        return self.deckOfCards_.pop()
    def cardsLeft(self):
        return len(self.deckOfCards_)
    
# ---------------- Testing ---------------- #

deck1 = Deck()
deck2 = Deck()
match_counter = 0 #counts the total matches found during the simulation
matched_cards = [] #maintains a list of matched cards found so far during the simulation
while deck1.cardsLeft() > 0:
    card1 = deck1.dealCard()
    card2 = deck2.dealCard()
    print(card1)
    print(card2)
    same_face_value = card1.getFaceValue() == card2.getFaceValue()
    same_suit = card1.getSuit() == card2.getSuit()
    if same_face_value and same_suit:
        match_counter += 1
        matched_cards.append(card1)
        print("We found a match!!!\n")
    else:
        print()
print("Total mathces found:",match_counter)
print("the card(s) matched is/are:")
for card in matched_cards:
    print(card)
