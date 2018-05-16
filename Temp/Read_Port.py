# ==========================================
# 功能：获取PC端的串口名称和串口号并返回端口号
# ==========================================
import serial
import serial.tools.list_ports
def Read_Port():
    com_list =[]
    port_list = list(serial.tools.list_ports.comports())
    for port in port_list:
        com_list.append(port[0])
    return com_list
    
#Read_Port()
