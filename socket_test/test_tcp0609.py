import socket

addr = ('192.168.1.101',10000)  # 目标主机IP
readdr = ('192.168.1.102', 10000)  # 本主机IP
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
