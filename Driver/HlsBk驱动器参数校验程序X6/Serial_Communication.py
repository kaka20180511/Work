"""
功能配置串口的波特率和超时检测时间
"""
import serial
def Ser_Com(num):
 # 配置串口
    serial.Serial(
        port=num,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5
    )
 
