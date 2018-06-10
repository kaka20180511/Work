# ==========================
# 功能：服务端程序，监听所有网卡
# 发到8888端口的消息
# ==========================
from socket import *
from threading import Thread

# 处理客户端的请求
def handle_client(client_socket, client_addr):
    while True:
        recv_data = client_socket.recv(1024)

        if len(recv_data) > 0:
            #print("[*] recv_data [%s]:%s" % (str(client_addr), recv_data.decode("gb2312")))
            print("收到%s客户端%s:%s" % (str(client_addr),"发来的消息",recv_data.decode("gb2312")))
            client_socket.send(bytes("收到！", "gb2312"))
        else:
            #print("[*] [%s] 客户端已断开！" % str(client_addr))
            print("[%s] 客户端已断开！" % str(client_addr))
            break

    client_socket.close()

def main():
    # 监听的网卡  0.0.0.0表示所有网卡
    bind_ip   = "0.0.0.0"
    bind_port = 8888

    server_socket = socket(AF_INET, SOCK_STREAM)

    # 实现端口复用
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    server_socket.bind((bind_ip, bind_port))
    server_socket.listen(5)

    try:
        while True:
            # 等待新的客户端
            client_socket, client_addr = server_socket.accept()

            #print("[*] 客户端连接成功：%s:%d"% (client_addr[0], client_addr[1]))
            print("客户端连接成功：%s:%d"% (client_addr[0], client_addr[1]))
            client_handle = Thread(target=handle_client, args=(client_socket, client_addr))
            client_handle.start()
            # 线程中是共享 client_socket 这个套接字的，所以此时执行 client_socket.close() 操作的话
            #会导致 client_socket 不在可用而出现错误

    finally:
        server_socket.close()

if __name__ == '__main__':
    main()
