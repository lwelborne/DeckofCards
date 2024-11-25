# Lenora Welborne
# CIS261
# DeckofCards
import random
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]
def deal_cards(deck, num_cards):
    dealt_cards = deck[:num_cards]
    remaining_deck = deck[num_cards:]
    return dealt_cards, remaining_deck
def main():
    print("Card Dealer")
    deck = create_deck()
    random.shuffle(deck)
    print(f"I have shuffled a deck of {len(deck)} cards.")
    while len(deck) > 0:
        try:
            num_cards = int(input("How many cards would you like? "))
            if num_cards > len(deck):
                print(f"There are only {len(deck)} cards left in the deck.")
                continue
            dealt_cards, deck = deal_cards(deck, num_cards)
            print("\nHere are your cards:") 
            for card in dealt_cards:
                print(card)
            print(f"\nThere are {len(deck)} cards left in the deck.")
        except ValueError:
            print("Please enter a valid number.")
        if len(deck) == 0:
            print("\nThe deck is empty. Thank you for playing!")
            break
        input("\nPress any key to continue...")
if __name__ == "__main__":
    main()