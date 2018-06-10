# =========================
# 功能：TCP客户端向网页请求数据
# =========================
import socket
target_host = "www.baidu.com"
target_port = 80
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((target_host, target_port))
client_socket.send(bytes("GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n", "utf-8"))
response = client_socket.recv(4096)
print("response:", response)
client_socket.close()
