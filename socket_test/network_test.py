# ==========================
# 廖雪峰的网络编程例子(客户端)
# ==========================
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.1.101', 9999))
# 接收欢迎消息:
#print (s.recv(1024).decode("utf-8"))
s.send(b"123456789")
#time.sleep(1)
read = s.recv(1024).decode("utf-8")
print(read)
read = s.recv(1024)
print(read)
#print (s.recv(1024).decode("utf-8"))
"""
for data in [b'Michael', b'Tracy', b'Sarah']:
    print(data)
    # 发送数据:
    s.send(data)
    print (s.recv(1024).decode("utf-8"))
"""
s.send(b'exit')
s.close()
