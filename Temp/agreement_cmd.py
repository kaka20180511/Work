# ===============================
# 功能是将协议命令拆分并返回命令列表
# ===============================
import binascii
def agreement_cmd():
    a = str('00030000000185DB')
    a_list = []
    for i in a.split():  # 拆分字符串
        a_list.append(binascii.a2b_hex(i))
    Data_Read = a_list 
    return Data_Read
