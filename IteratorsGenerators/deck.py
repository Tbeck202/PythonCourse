from random import shuffle


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    # this function makes it possible to iterate over the Deck object as opposed to using Deck.cards (or self.cards)
    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        if count == 0:
            raise ValueError("all cards have been dealt")
        actual = min([count, num])  # sets actual to the lower of num and count
        # next, slice from the end of the list. Essentially popping the last three cards
        cards = self.cards[-actual:]
        # then slice from the begginning to update the deck with the last three cards having been removed
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
print(d)
for card in d:
    print(card)
