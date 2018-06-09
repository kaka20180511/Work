# ===========================
# 功能：将IPV4地址转换成不同的
# 格式
# ===========================
import socket
from binascii import hexlify
def convert_ip4_address():
    for ip_addr in ["127.0.0.1", "192.168.0.1"]:
        # 将IP地址转换成二进制数的IP地址
        packed_ip_addr = socket.inet_aton(ip_addr)
        # 将二进制数的IP地址转换成IP地址
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address: %s => packed: %s,Unpacked: %s" %(ip_addr,hexlify(packed_ip_addr),unpacked_ip_addr))
        
if __name__ == "__main__":
    convert_ip4_address()
