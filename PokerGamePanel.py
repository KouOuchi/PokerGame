from PyQt5.QtQuick import QQuickItem
from PyQt5 import QtCore
from PokerGameEngine import PokerGameEngine

class PokerGamePanel(QQuickItem):
    
    def __init__(self, parent=None):
        super().__init__(parent)              
        self.engine = PokerGameEngine()
        self.credit = 10000
        self.status = 'Wait for start.'

    def get_credit(self):
        """
        pass to property
        """
        return self.credit  
    
    def set_credit(self, value):
        """
        pass to property
        """
        self.credit = value
        self.current_creditChanged.emit(self.credit)

    current_creditChanged = QtCore.pyqtSignal(int)
    current_credit = QtCore.pyqtProperty(int, get_credit, set_credit, notify=current_creditChanged)
    
    def get_status(self):
        """
        pass to property
        """
        return self.status

    def set_status(self, value):
        """
        pass to property
        """
        self.status = value
        self.current_statusChanged.emit(self.status)

    current_statusChanged = QtCore.pyqtSignal(str)
    current_status = QtCore.pyqtProperty(str, get_status, set_status, notify=current_statusChanged)

    @QtCore.pyqtSlot(int)
    def draw_start(self, bet):
        # build deck and hand
        self.engine.draw()
      
        # check hand
        self.engine.check_hand()
        
        # charge
        self.set_credit(self.credit - bet)
        
        if self.engine.hand.is_royale_flush():
            self.set_status('Winner! Winner! Royale Flush!')
            return

        if self.engine.hand.is_straight_flush():
            self.set_status('Winner!!!! Straight Flush.')
            return

        if self.engine.hand.is_full_house():
            self.set_status('Winner!!! Full House.')
            return

        if self.engine.hand.is_four_of_a_kind():
            self.set_status('Winner!! 4 of a Kind.')
            return

        if self.engine.hand.is_flush():
            self.set_status('Winner!! Flush.')
            return

        if self.engine.hand.is_straight():
            self.set_status('Winner!! Straight.')
            return

        if self.engine.hand.is_three_of_a_kind():
            self.set_status('Winner! 3 of a Kind.')
            return

        if self.engine.hand.is_two_pair():
            self.set_status('Winner! 2 Pair.')
            return

        if self.engine.hand.is_a_pair():
            self.set_status('Winner. A Pair.')
            return

        if(self.credit == 0):
            self.set_status('Bankruptcy.')
        else:
            self.set_status('Wait for start.')
                
    @QtCore.pyqtSlot(int, result=str)
    def get_hand(self, no):       
        """
        Get 1 Card from Hand
        
        Parameters
        ----------
        no : int
            index of card of hand

        Returns
        -------
        str
            relative path of image
        """
        if not self.engine.hand:
            QtCore.qDebug('Unexpected. Hand is None.')
            self.set_status('Error.')
            return None
        if no < 0 or len(self.engine.hand.cards) <= no:
            QtCore.qDebug('Unexpected. Number of cards failure.')
            self.set_status('Error.')
            return None

        display_card = self.engine.hand.cards[no]
        
        return display_card.image_source()
