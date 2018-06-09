# ==========================
# 廖雪峰的网络编程例子(服户端)
# ==========================

import time, socket, threading

def tcplink(sock, addr):
    print ('有客户端接入 %s:%s...' % addr)
    sock.send(b"ok")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data .decode("utf-8")  == 'exit':
            break
        sock.send(("Hello,%s!"% data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print ('客户端断开连接 %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('192.168.1.101', 9999))
s.listen(5)
#print ('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
