# Lenora Welborne
# CIS261
# DeckofCards
import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self, number_of_cards):
        if number_of_cards > len(self.deck):
            raise ValueError("Not enough cards in the deck to deal.")
        dealt_cards = self.deck[number_of_cards:]
        self.deck = self.deck[number_of_cards:]
       
        return dealt_cards
    def count(self):
        return len(self.deck)
def card_dealer():
    print("Card Dealer")
    deck = Deck()
    deck.shuffle()
    print(f"I have shuffled a deck of {deck.count()} cards.")
    while True:
        try:
            number_of_cards = int(input("How many cards would you like?: "))
            if number_of_cards <= 0 or number_of_cards > deck.count():
                print(f"Please enter a number between 1 and {deck.count()}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    dealt_cards = deck.deal(number_of_cards)
    print("\nHere are your cards:")
    for card in dealt_cards:
        print(card)
    print(f"\nThere are {deck.count()} cards left in the deck.")
    print("\nGood luck!")
  
card_dealer()
