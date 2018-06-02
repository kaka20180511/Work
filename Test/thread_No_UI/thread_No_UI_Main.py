import serial
import threading
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

class main():
    def __init__():
        super().__init__()
        
    def main_data():
        sum = Sum()
        sum.sinOut.connect(printNum)  # 将信号连接至printNum函数
        sum.start()  # 开启线程
        
    def printNum(num):
        print(str(num))
        #self.textEdit.append(str(num))
        #self.lable.setText(str(num))
        
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
                                timeout=5
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

        
        print(num)



        
