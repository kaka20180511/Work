# ==========================
# 功能：简单的客户端
# ==========================
import socket
# 创建一个基于IPv4和TCP协议的socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
phone.connect(('192.168.1.101',9999)) #拨通电话
# 发送消息
phone.send('hello'.encode('utf-8')) #发消息
# 阻塞，等待返回的消息
back_msg=phone.recv(1024)
print(back_msg)

phone.close()
