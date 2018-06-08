# ===============================
# 功能：解析车辆状态并返回给主函数
# 将执行命令、限位、陀螺仪、货架、
# 二维码、电机全部拆分用子函数解析
# 2018/05/31  lsl
# ===============================

# ===============================
# 功能：截取2-4字符然后转换成二进制
def Hex_Conversion_Binary(data):
    try:
        # Intercept AGV status field
        Data_Hex = (data)[2:4]  
        # Converts hexadecimal characters to binary numbers
        Data_Binary = (bin(int(Data_Hex, 16)))[2:]  
        # Complement digit
        Data_Binary_Complete = Data_Binary.zfill(8)  
        # Data bit flip
        Complete_Binary = Data_Binary_Complete[::-1]  
        return Complete_Binary
    except:
        print("十六进制转二进制出错")
# ===============================

# ===============================
# 功能：解析AGV命令执行状态（bit0~
# bit1）
def status_cmd(data):
    try:
        AGV_status_cmd = Hex_Conversion_Binary(data)
        # Decode 0-2 bit
        if AGV_status_cmd[0:2] == "00":
            AGV_status_cmd_describe = "命令执行完成"
            
        if AGV_status_cmd[0:2] == "10":
            AGV_status_cmd_describe = "命令执行中"
        
        if AGV_status_cmd[0:2] == "01":
            AGV_status_cmd_describe = "接收到错误指令"
            
        if AGV_status_cmd[0:2] == "11":
            AGV_status_cmd_describe = "指令因错误而终止"
            
        return AGV_status_cmd_describe
            
    except:
        print("解析AGV命令执行状态出错")
# ===============================

# ===============================
# 功能：解析AGV托盘限位状态（status_ls）
def status_ls(data):
    try:
        AGV_status_ls = Hex_Conversion_Binary(data)
        if AGV_status_ls[2:3] == "0":
            AGV_status_ls_describe = "托盘限位未确认"
            
        if AGV_status_ls[2:3] == "1":
            AGV_status_ls_describe = "托盘限位已确认"
        return AGV_status_ls_describe
        
    except:
        print("解析AGV托盘限位状态出错")
# ===============================

# ===============================
# 功能：解析陀螺仪状态（status_gyrozero）
def status_gyrozero(data):
    try:
        AGV_status_gyrozero = Hex_Conversion_Binary(data)
        if AGV_status_gyrozero[3:4] == "0":
            AGV_staus_gyrozero_describe = "陀螺零偏纠正中"
            
        if AGV_status_gyrozero[3:4] == "1":
            AGV_staus_gyrozero_describe = "陀螺零偏纠正完成"
        return AGV_staus_gyrozero_describe
        
    except:
        print("解析AGV陀螺仪状态出错")
# ===============================

# ===============================
# 功能：解析AGV带货架状态（status_bucket）
def status_bucket(data):
    try:
        AGV_status_bucket = Hex_Conversion_Binary(data)
        if  AGV_status_bucket[4:6] == "00":
            AGV_status_bucket_describe = "没带货架"
            
        if  AGV_status_bucket[4:6] == "10":
            AGV_status_bucket_describe = "带货架"
            
        if  AGV_status_bucket[4:6] == "01":
            AGV_status_bucket_describe = "不确定"
            
        return AGV_status_bucket_describe
        
    except:
        print("解析AGV带货架状态出错")
# ===============================

# ===============================
# 功能：解析下视读码状态（status_barcode）
def status_barcode(data):
    try:
        AGV_status_barcode = Hex_Conversion_Binary(data)
        if AGV_status_barcode[6:7] == "1":
            AGV_status_barcode_describe = "在码上"
            
        if AGV_status_barcode[6:7] == "0":
            AGV_status_barcode_describe = "不在码上"
        return AGV_status_barcode_describe
        
    except:
        print("解析下视读码状态出错")
# ===============================

# ===============================
# 功能：解析读电机状态（status_motorenable）
def status_motorenable(data):
    try:
        AGV_status_motorenable = Hex_Conversion_Binary(data)
        if AGV_status_motorenable[7:8] == "0":
            AGV_status_motorenable_describe = "电机关闭"
            
        if AGV_status_motorenable[7:8] == "1":
            AGV_status_motorenable_describe = "电机打开"
        return AGV_status_motorenable_describe
        
    except:
        print("解析下视读码状态出错")
# ===============================

