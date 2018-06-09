# ===========================
# 功能：处理套接字错误
# ===========================
import sys
import socket
import argparse
def main():
    parser = argparse.ArgumentParser(description = "Socket Error Examples")
    parser.add_argument("--host", action = "store", dest = "host", required = False)
    parser.add_argument("--port", action = "store", dest = "port", type = int , required = False)
    
