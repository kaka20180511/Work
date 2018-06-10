# ======================
# 功能：简单的聊天工具，测试
# 一下局域网TCP通信
# ======================
import socket
traget_host = "192.168.1.100"
traget_port = 6688

# 建立socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# traget_host、traget_port以元组的形式传入connect()函数
client_socket.connect((traget_host, traget_port))
data = "你好！"
client_socket.send(data.encode("gb2312"))
recv_data = client_socket.recv(1024)
print("recv_data:%s"%recv_data)
client_socket.close()
