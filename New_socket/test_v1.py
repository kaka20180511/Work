# =========================
# 功能：创建一个简单的tcp服务端
# =========================
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.bind(('0.0.0.0',9999)) #插电话卡

phone.listen(5) #开机，backlog

print('starting....')
conn,addr=phone.accept() #接电话
print(conn)
print('client addr',addr)
print('ready to read msg')
client_msg=conn.recv(1024) #收消息
print('client msg: %s' %client_msg)
conn.send(client_msg.upper()) #发消息

conn.close()
phone.close()
