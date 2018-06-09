# ==============================
# 功能：获取本机名称及IP地址，如有多
# 个地址，只能获取其中一个
# ==============================
import socket
def print_machine_info():
    # 返回本地主机的名字
    host_name = socket.gethostname()
    # 返回本地主机的IP
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s"%host_name)
    print("IP address:%s"%ip_address)
    
if __name__ == "__main__":
    print_machine_info()
