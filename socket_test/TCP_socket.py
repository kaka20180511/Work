# =========================
# 简单的带界面客户端
# =========================

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_TCP_socket import Ui_MainWindow
from modify_TCP import *

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 刚启动程序时发送按钮变、断开按钮成不可选
        self.pushButton_Send.setEnabled(False)
        self.pushButton_interrupt.setEnabled(False)
    # 连接按钮
    @pyqtSlot()
    def on_pushButton_Connect_clicked(self):
        # 为防误操作，当连接按钮按下时连接按钮变得不可选，发送按钮、断开按钮变得可选
        self.pushButton_Connect.setEnabled(False)
        self.pushButton_Send.setEnabled(True)
        self.pushButton_interrupt.setEnabled(True)
        # 获取用户输入的IP地址
        self.input_IP = self.lineEdit_IP_add.text()
        print(self.input_IP)
        connect_get(self.input_IP)
        pass
    # 断开按钮
    @pyqtSlot()
    def on_pushButton_interrupt_clicked(self):
        # 为防误操作，当断开按钮按下时发送按钮、断开按钮变得不可选，连接按钮变得可选
        self.pushButton_Send.setEnabled(False)
        self.pushButton_Connect.setEnabled(True)
        self.pushButton_interrupt.setEnabled(False)
        close_connect()
        pass
    
    @pyqtSlot()
    def on_pushButton_Send_clicked(self):
        self.input_data = self.textEdit_Send.toPlainText() 
        print(self.input_data)
        
        self.textEdit_Receive.append(send_to(self.input_data))
        pass
        
        
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
