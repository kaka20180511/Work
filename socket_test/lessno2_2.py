import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = socket.getservbyname("http", "tcp")

s.connect(("baidu.com", port))
print(s.getsockname)
print(s.getpeername)
