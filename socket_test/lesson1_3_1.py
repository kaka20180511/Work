# ==========================
# 功能：获取远程设备的IP地址
# ==========================

import socket
def get_remote_machine_info():
    remote_host = "www.python.org"
    try:
        print("IP address:%s" %socket.gethostbyname(remote_host))
    except:
        print("remote_host error")
        
if __name__ == "__main__":
    get_remote_machine_info()
        
    
