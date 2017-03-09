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

    def pop_card_by_index(self, index=-1):
        return self._cards.pop(index)

    def pop_card(self, card: Card):
        return self.pop_card_by_index(self.card_index(card))

    def card_index(self, card: Card):
        for index, _card in enumerate(self._cards):
            if card.rank == _card.rank and card.suit == _card.suit:
                break
        else:
            raise ValueError('Card not found')

        return index

    def draw_cards(self, other_deck: 'Deck', number=1):
        for _ in range(number):
            other_deck.add_card(self.pop_card_by_index())

    def move_card(self, other_deck: 'Deck', card: Card):
        other_deck.add_card(self.pop_card(card))

class Hand(Deck):

    def __init__(self):
        self._cards = []

class PlayDeck(Deck):

    def __init__(self):
        self._cards = []

deck = Deck()
handa = Hand()
playdec = PlayDeck()

random.shuffle(deck)

deck.move_card(handa, Card('10', 'Cerveny'))

print(len(deck))
print('{:*^30}'.format('Hand'))
print(list(handa))

# carda = Card('Svindl', 'zolik')
# deck.add_card(carda)
# print(deck[-1])