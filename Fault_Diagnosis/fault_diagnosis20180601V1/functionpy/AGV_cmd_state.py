# ===============================
# 功能：解析车辆命令状态并返回给主函
# 数,将命令ID、数据帧、是否休眠、上
# 电是否收到摄像头数据、工作模式，全
# 部拆分用子函数解析。
# 2018/05/31  lsl
# ===============================
# ===============================
# 功能：截取4-6字符然后转换成二进制
def Hex_Conversion_Binary(data):
    try:
        # Intercept AGV status field
        Data_Hex = (data)[4:6]  
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
# 功能：解析AGV命令ID号（bit0~bit3）
def cmd_ID(data):
    try:
        # Decode 0-4 bit
        AGV_cmd_ID = (Hex_Conversion_Binary(data))[0:4]
        #print(AGV_cmd_ID)
        # 将二进制数据翻转
        AGV_cmd_ID = AGV_cmd_ID[::-1]
        # 二进制转十进制
        AGV_cmd_ID_D = int(AGV_cmd_ID, 2)
        return AGV_cmd_ID_D
    except:
        print("解析AGV命令执行状态出错")
# ===============================

# ===============================
# 功能：解析AGV数据帧状态（data_frame）
def data_frame(data):
    try:
        AGV_data_frame = Hex_Conversion_Binary(data)
        if AGV_data_frame[4:5] == "0":
            AGV_data_frame_describe = "正常帧"
            
        if AGV_data_frame[4:5] == "1":
            AGV_data_frame_describe = "特殊帧"
        return AGV_data_frame_describe
        
    except:
        print("解析AGV数据帧状态出错")
# ===============================

# ===============================
# 功能：解析AGV是否休眠状态（sleepFlag）
def sleepFlag(data):
    try:
        AGV_sleepFlag = Hex_Conversion_Binary(data)
        if AGV_sleepFlag[5:6] == "0":
            AGV_sleepFlag_describe = "运行"
            
        if AGV_sleepFlag[5:6] == "1":
            AGV_sleepFlag_describe = "休眠"
        return AGV_sleepFlag_describe
        
    except:
        print("解析AGV是否休眠状态出错")
# ===============================

# ===============================
# 功能：解析AGV摄像头数据状态（CameraDataValid）
def CameraDataValid(data):
    try:
        AGV_CameraDataValid = Hex_Conversion_Binary(data)
        if AGV_CameraDataValid[6:7] == "0":
            AGV_CameraDataValid_describe = "上电未收到摄像头"
            
        if AGV_CameraDataValid[6:7] == "1":
            AGV_CameraDataValid_describe = "上电收到摄像头数据"
        return AGV_CameraDataValid_describe
        
    except:
        print("解析AGV是否休眠状态出错")
# ===============================

# ===============================
# 功能：解析AGV运行状态（CameraDataValid）
def RunMode(data):
    try:
        AGV_RunMode = Hex_Conversion_Binary(data)
        if AGV_RunMode[7:8] == "0":
            AGV_RunMode_describe = "正常模式"
            
        if AGV_RunMode[7:8] == "1":
            AGV_RunMode_describe = "Debug模式"
        return AGV_RunMode_describe
        
    except:
        print("解析AGV运行状态出错")
# ===============================
