# =======================================
# socket 通信测试（服户端）
import socket  
address = ("30.113.146.245",10000)#本主机IP  
readdr = ("30.113.146.4",10000)#客户端主机IP  
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
  
s.bind(address)  
while 1:  
    data,addr=s.recvfrom(2048)  
    if not data:  
        break  
    print("got data from",addr)  
    print(data.decode())  
    replydata = input("这是服务端，请输入回复消息:")  
    s.sendto(replydata.encode("utf-8"),readdr)  
s.close()  
