
import sys
from PyQt5.QtWidgets import QApplication,QWidget, QMainWindow
#from PyQt5 import QtCore
from PyQt5.QtCore import *

import threading
import time
import pygame
from pygame.locals import *
from sys import exit


from PyQt5.QtCore import pyqtSlot

from Ui_testV5 import Ui_MainWindow
from Test.testV5 import *


class MainWindow(QMainWindow, Ui_MainWindow, QWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    def keyPressEvent(self, event):


        print("按下：" + str(event.key()))
        # 举例组合键按下
        if (event.key() == Qt.Key_W):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + W")
            else :
                print("W")
        if (event.key() == Qt.Key_A):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + A")
            else :
                print("A")
        if (event.key() == Qt.Key_D):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + D")
            else :
                print("D")
        if (event.key() == Qt.Key_S):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + S")
            else :
                print("S")
        # 举例单键按下
        if(event.key() == Qt.Key_Shift):
            print("测试：Shift")
        if(event.key() == Qt.Key_Escape):
            print('测试：ESC')
        if(event.key() == Qt.Key_A):
            print('测试：A')
        if(event.key() == Qt.Key_W):
            print('测试：W')
        if(event.key() == Qt.Key_Enter):
            print('测试：Enter')
        if(event.key() == Qt.Key_Space):
            print('测试：Space')

    @pyqtSlot()
    def on_pushButton_connect_clicked(self):
       print("连接")
        
if __name__ =="__main__":
   
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
