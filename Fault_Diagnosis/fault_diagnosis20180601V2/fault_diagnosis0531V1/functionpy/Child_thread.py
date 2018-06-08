# ==========================================
# 功能：创建一个子线程，并接收原始数据，（已
# 丢弃不完整的数据帧
import sys
import random
import threading
import time
import serial
import binascii
from PyQt5.QtCore import pyqtSlot

class Sum(QThread):
    ok_data = ''
    Error = ''
    Repeat_Data = ''
    # self.Raw_Data = []
    sinOut = pyqtSignal(str)
    global ser

    def __init__(self):
        super().__init__()
        self.m = 0

    def run(self):
        try:
            while (True):
                self.num = 0
                # n = ser.inWaiting()
                # print(n)
                self.data_D = binascii.b2a_hex(ser.read(1))  # 将ASCII码的字符串转换成十六进制
                # print(self.data_D)
                self.data = str(self.data_D.decode('utf-8'))  # 去掉字符串前面的符号"b"
                # print(self.data_D)
                # print(self.data)
                if self.data == "aa":  # 寻找帧头
                    # 找到帧头后将帧头和数据部分拼接在一起
                    while (True):
                        if self.data == "55" and self.num == 47:  # 判断是否是完整的一帧
                            self.ok_data = self.ok_data + "55"  # 将帧尾拼接到数据帧上
                            self.sinOut.emit(self.ok_data)  # 发射信号并将数据一并发送
                            self.ok_data = ''  # 清空上一帧数据
                            break

                        self.ok_data = self.ok_data + self.data  # 每一帧数据拼接
                        print(self.ok_data)
                        self.num = self.num + 1  # 数据个数计数
                        # print(self.num)
                        if self.num > 48 or len(self.ok_data) > 100:
                            self.ok_data = ''
                            self.num = 0
                        self.data_D = binascii.b2a_hex(ser.read(1))  # 将ASCII码的字符串转换成十六进制
                        self.data = str(self.data_D.decode('utf-8'))  # 去掉字符串前面的符号"b"
                        # print(self.data)

                # self.sleep(0.5)

                time.sleep(0.05)
        except:
            ser.close()
            print("串口异常")
            # self.textEdit_AbnormalInformation.append("串口异常")
