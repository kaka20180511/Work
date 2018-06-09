# ===========================
# 功能：主机字节序和网络字节序之间
# ===========================
import socket
def conver_integer():
    data = 1234
    print("Original:%s => Long host byte order:%s,Network byte order:%s"%(data, socket.ntohl(data), socket.htonl(data)))
    print("Original:%s => Short host byte order:%s,Network byte order:%s"%(data, socket.ntohs(data), socket.htons(data)))
    
if __name__ == "__main__":
    conver_integer()
    
    
