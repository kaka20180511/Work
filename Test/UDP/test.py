# ============================================
# socket通信测试（客户端）
import socket

addr = ('192.168.35.147', 10000)  # 目标主机IP
readdr = ('192.168.35.140', 10000)  # 本主机IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(readdr)
while 1:

    data = input("input:")
    if not data:
        break
    s.sendto(data.encode("utf-8"), addr)

    recivedata, addrg = s.recvfrom(2048)
    if recivedata:
        print("from:", addrg)
        print("got recive :", recivedata.decode())
s.close()