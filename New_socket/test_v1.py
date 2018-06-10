# =========================
# 功能：创建一个简单的tcp服务端
# =========================
# 导入socket库
import socket
# 创建一个基于IPv4和TCP协议的Socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
# 监听端口（"0.0.0.0"代表所有本地的IP）
phone.bind(('0.0.0.0',9999)) #插电话卡
# 调用listen（）方法开始监听端口，传入的参数指定等待连接的最大数量
phone.listen(5) #开机，backlog

print('starting....')
# 建立客户端连接（accept为被动接受TCP客户端连接，（阻塞式）等待连接的到来）
conn,addr=phone.accept() #接电话
print(conn)
print('client addr',addr)
print('ready to read msg')
# recv（）为接收客户端发来的数据
client_msg=conn.recv(1024) #收消息
print('client msg: %s' %client_msg)
# send（）为发送数据到客户端
conn.send(client_msg.upper()) #发消息

conn.close()
phone.close()
