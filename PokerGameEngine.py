from Deck import Deck

class PokerGameEngine:
    """
    poker game engine
    """

    def __init__(self):
        self.hand = None
        self.deck = None

    def draw(self):
        self.deck = Deck()

        # get Hand from Deck
        self.hand = self.deck.create_hand()

        # debug output
        for c in self.hand.cards:
            print(c.card_figure())

    def check_hand(self):
        return self.hand.check()
