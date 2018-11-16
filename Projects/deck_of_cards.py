from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.cards = [Card(value, suit)
                      for value in Deck.values for suit in Deck.suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt")
        number_of_cards_to_deal = min([count, number])
        cards_to_deal = self.cards[-number_of_cards_to_deal:]
        self.cards = self.cards[:-number_of_cards_to_deal]
        return cards_to_deal

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


deck = Deck()
print(deck)  # 'Deck of 52 cards'

deck.shuffle()
print(deck.cards)  # e.g. [5 of Spades, J of Clubs, ...]

card = deck.deal_card()
print(card)  # e.g. 'J of Hearts

hand = deck.deal_hand(5)
print(hand)
# e.g. [7 of Hearts, 9 of Hearts, Q of Clubs, 10 of Clubs, J of Clubs]

for card in deck:
    # if class does not contain __iter__ method -> TypeError: 'Deck' object is not iterable
    print(card)
