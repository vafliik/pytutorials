import random
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class Deck:

    suits = "Kule Zeleny Zaludy Cerveny".split()
    ranks = [str(n) for n in range(7, 11)] + "Spodek Svrsek Kral Eso".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def add_card(self, card: Card):
        self._cards.append(card)

    def pop_card(self, index=-1):
        return self._cards.pop(index)

    def draw_cards(self, hand: 'Hand', number=1):
        for _ in range(number):
            hand.add_card(self.pop_card())

class Hand(Deck):

    def __init__(self):
        self._cards = []

deck = Deck()
handa = Hand()


print(len(deck))
random.shuffle(deck)
print(list(deck)[-5:])

carda = Card('Svindl', 'zolik')
deck.add_card(carda)
print(deck[-1])