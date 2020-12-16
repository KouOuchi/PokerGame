class Card:
    """
    One trump card
    """
    # suit list
    SUITS = ['diamond', 'heart', 'spade', 'clover']

    def __init__(self, _suit, _rank):
        # check suits from SUITS
        if not _suit in Card.SUITS:
            raise RuntimeError('Invalid suit.')

        # check rank
        if _rank < 1 or 13 < _rank:
            raise RuntimeError('Invalid rank.')

        self.suit = _suit
        self.rank = _rank

    def dump(self):
        print("suit : {}, rank : {}".format(self.suit, self.rank))

    def card_figure(self):
        """
        create ascii information
        """
        suit_char = ''
        if self.suit == Card.SUITS[1]:
            suit_char = '♥'
        elif self.suit == Card.SUITS[0]:
            suit_char = '♦'
        elif self.suit == Card.SUITS[2]:
            suit_char = '♠'
        elif self.suit == Card.SUITS[3]:
            suit_char = '♣'
        else:
            raise Exception()

        rank_char = ''
        if self.rank == 11:
            rank_char = 'J'
        elif self.rank == 12:
            rank_char = 'Q'
        elif self.rank == 13:
            rank_char = 'K'
        else:
            rank_char = str(self.rank)

        return suit_char + rank_char

    def image_source(self):
        """
        get relative path of image file
        """
        path = 'image/'
        if self.suit == 'heart':
            path += '2'
        elif self.suit == 'diamond':
            path += '1'
        elif self.suit == 'spade':
            path += '3'
        elif self.suit == 'clover':
            path += '0'
        else:
            raise Exception()

        path += '_' + str(self.rank - 1) + '.png'

        return path
