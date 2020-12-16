from Card import Card
from Hand import Hand
from random import shuffle

class Deck:
    """
    52 trump deck
    """
    def __init__(self):
        self.cards = []

        # build 52 cards
        for my_suit in Card.SUITS:
            for my_rank in range(1, 14):
                self.cards.append(Card(my_suit, my_rank))

        # shuffle ordered cards
        shuffle(self.cards)

    def create_hand(self):
        """
        pop 5 cards from self.cards

        Returns
        -------
        my_hand : Hand instance
        """
        print("card len")
        print(len(self.cards))

        my_hand = Hand()
        for index in range(5):
            my_hand.add_card(self.cards.pop())

        print("card len")
        print(len(self.cards))
        print("hand len")
        print(len(my_hand.cards))
        return my_hand
