from Card import Card

class Hand:
    """
    5 trump cards and some flags of poker hand
    """
    def __init__(self):
        self.cards = []

        # poker hand flags
        self.hand_is_a_pair = False
        self.hand_is_two_pair = False
        self.hand_is_three_of_a_kind = False
        self.hand_is_four_of_a_kind = False
        self.hand_is_straight = False
        self.hand_is_flush = False
        self.hand_is_royale = False

    def check(self):
        """
        set some flags of poker hand
        """
        pass

    def add_card(self, _card):
        """
        Add one Card instance
        """
        self.cards.append(_card)

    def print_hand(self):
        """
        debug print

        Returns
        -------
        None.

        """
        line = ""
        for cd in self.cards:
            line += cd.card_figure()
            line += ' '

        print(line)

    def is_a_pair(self):
        return self.hand_is_a_pair

    def is_two_pair(self):
        return self.hand_is_two_pair

    def is_three_of_a_kind(self):
        return self.hand_is_three_of_a_kind;

    def is_four_of_a_kind(self):
        return self.hand_is_four_of_a_kind;

    def is_straight(self):
        return self.hand_is_straight;

    def is_flush(self):
        return self.hand_is_flush;

    def is_full_house(self):
        return self.is_a_pair() and self.is_three_of_a_kind()

    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_royale_flush(self):
        return self.is_straight_flush() and self.hand_is_royale
