from random import shuffle


class Card:

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    values = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        deck = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(suit, value)
                deck.append(card)
        self.deck = deck

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.deck)

    def _deal(self, num_cards):
        deal_num = 0
        deal = []
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif num_cards > self.count():
            for card in self.deck:
                c = self.deck.pop()
                deal.append(c)
            return deal
        else:
            while deal_num < num_cards:
                card = self.deck.pop(0)
                deal.append(card)
                deal_num += 1
            return deal

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.deck)

    def deal_card(self):
        card = self._deal(1)
        for c in card:
            return c

    def deal_hand(self, num_cards):
        hand = self._deal(num_cards)
        return hand


deck1 = Deck()

deck1.shuffle()
print(deck1.deal_hand(51))
print(deck1.count())
print(deck1.deal_hand(5))
print(deck1.count())
print(deck1.deal_hand(5))

# deck1.shuffle()
# print(deck1.deal_card())
# print(deck1.deal_card())
# print(deck1.deal_card())

# deck1.shuffle()
# print(deck1._deal(5))
# deck1.shuffle()

# print(deck1.count())
# deck1.shuffle()
# print(deck1._deal(52))

# print(deck1._deal(51))
# print(deck1.count())
# print(deck1._deal(5))
# print(deck1.count())
# print(deck1._deal(2))

# def _deal(self, num_cards):
#         deal_num = 0
#         deal = []
#         if self.count() == 0:
#             raise ValueError("All cards have been dealt")
#         elif num_cards > self.count():
#             # return [card for card in self.deck]
#             for card in self.deck:
#                 c = self.deck.pop()
#                 deal.append(c)
#                 return deal
#         else:
#             while deal_num < num_cards:
#                 card = self.deck.pop(0)
#                 deal.append(card)
#                 deal_num += 1
#             return deal
