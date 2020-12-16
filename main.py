import os
import sys
from PyQt5 import QtCore
from PyQt5.QtQml import QQmlApplicationEngine,qmlRegisterType
from PyQt5.QtWidgets import QApplication
from PokerGamePanel import PokerGamePanel
# import resource from qrc
from PokerGameQrc import *

def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'Info'
    elif mode == QtCore.QtWarningMsg:
        mode = 'Warning'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'critical'
    elif mode == QtCore.QtFatalMsg:
        mode = 'fatal'
    else:
        mode = 'Debug'
    print("%s: %s (%s:%d, %s)" % (mode, message, context.file, context.line, context.file))

def main():
    qmlRegisterType(PokerGamePanel, 'PokerGamePanel', 1, 0, 'PokerGamePanel')
    
    QtCore.qInstallMessageHandler(qt_message_handler)
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine(app)
    
    qml = os.path.join(os.path.dirname(__file__), 'qml/RootWindow.qml')
    engine.load(qml)
    if len(engine.rootObjects()) == 0:    
         print("Loading QML Error.")
         return
    
    app.exec_()

if __name__ == '__main__':
    main()
