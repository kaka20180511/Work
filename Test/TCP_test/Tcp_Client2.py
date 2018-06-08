import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)

conn,address = sk.accept()
sk.sendall(bytes("Hello world",encoding="utf-8"))


"""
import socket

obj = socket.socket()
obj.connect(("127.0.0.1",8080))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)

"""
