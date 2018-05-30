import sys
import time
import serial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow


from Ui_thread_test import Ui_MainWindow


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
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.sum = Sum()  # 实例化Sum类
        self.sum.sinOut.connect(self.printNum)  # 将信号连接至printNum函数
        self.sum.start()  # 开启线程
        pass
        
    def printNum(self, num):
        self.textEdit.append(str(num))
        #self.lable.setText(str(num))
        
        print(num)
        
class Sum(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.m = 0

    def run(self):
        try:
            ser = serial.Serial(port="COM2",
                                baudrate=9600,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1
                                )
            while (1):
                self.m = str(ser.read(48))
                print(self.m)
                #self.sleep(0.5)
                self.sinOut.emit(self.m)
                time.sleep(1)
        except:
            ser.close()
            print("串口异常")


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
