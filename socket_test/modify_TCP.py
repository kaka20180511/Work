import socket
# 建立socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接函数
def connect_get(IP):
    traget_host = IP
    traget_port = 8888
    # traget_host、traget_port以元组的形式传入connect()函数
    client_socket.connect((traget_host, traget_port))


def send_to(data):
    # 采用gb2312的编码格式是因为要发送中文
    client_socket.send(data.encode("gb2312"))
    # 接收服务端返回的数据
    recv_data = client_socket.recv(1024)
    print("recv_data:%s"%recv_data.decode("gb2312"))
    return recv_data.decode("gb2312")
    
    

def close_connect():
    # 收到消息后关闭客户端端口
    client_socket.close()

if __name__ == "__main__":
    connect_get("192.168.1.102")
    send_to("你好吗！")
    close_connect()
