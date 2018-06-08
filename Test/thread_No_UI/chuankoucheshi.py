import serial  
import time   
from PyQt5.QtCore import pyqtSlot  
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
