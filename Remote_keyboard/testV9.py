# ========================
# 功能：实现键盘按键和鼠标的监控
# ======================== 

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import *
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.setWindowTitle('按键检测')
        self.show()
 
    # 检测键盘回车按键
    def keyPressEvent(self, event):
        print("按下：" + str(event.key()))
        # 举例组合键按下
        if (event.key() == Qt.Key_W):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                print("shift + W")
            else :
                print("W")
        # 举例单键按下
        if(event.key() == Qt.Key_Escape):
            print('测试：ESC')
        if(event.key() == Qt.Key_A):
            print('测试：A')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("鼠标左键点击")
        elif event.button() == Qt.RightButton:
            print("鼠标右键点击")
        elif event.button() == Qt.MidButton:
            print("鼠标中键点击")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
