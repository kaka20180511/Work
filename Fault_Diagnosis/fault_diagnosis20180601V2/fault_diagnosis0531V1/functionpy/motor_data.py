# ===============================
# 功能：解析AGV指令速度与实际速度值
# 2018/6/1 wm
# ===============================
# ***************************************************************************************************#
# 解析小车指令速度，获取小车左右轮指令速度，再除以2得到小车指令速度

def Left_CMD_Speed_Analysis(data):
    try:
        AGV_CMD_Left_Speed = data[36:40]  # 截取车辆左轮指令速度字段
        AGV_CMD_Left_Speed = int(AGV_CMD_Left_Speed, 16)
        AGV_CMD_Left_Speed_minus = AGV_CMD_Left_Speed & 32768
        if AGV_CMD_Left_Speed_minus != 0:
            AGV_CMD_Left_Speed = ((~AGV_CMD_Left_Speed) & 0xffff) + 1  # 等于1
            AGV_CMD_Left_Speed = AGV_CMD_Left_Speed * -1
        return str(AGV_CMD_Left_Speed)
    except:
        print("左轮指令速度解析出错")
####################################################################
def Right_CMD_Speed_Analysis(data):
    try:
        AGV_CMD_Right_Speed = data[40:44]  # 截取车辆右轮指令速度字段
        AGV_CMD_Right_Speed = int(AGV_CMD_Right_Speed, 16)
        AGV_CMD_Right_Speed_minus = AGV_CMD_Right_Speed & 32768
        if AGV_CMD_Right_Speed_minus != 0:
            AGV_CMD_Right_Speed = ((~AGV_CMD_Right_Speed) & 0xffff) + 1  # 等于1
            AGV_CMD_Right_Speed = AGV_CMD_Right_Speed * -1
        
        return str(AGV_CMD_Right_Speed)
        
    except:
        print("右轮指令速度解析出错")
        
def AGV_CMD_Speed(data):
    try:
        LeftCMDSpeed = Left_CMD_Speed_Analysis(data)
        RightCMDSpeed =  Right_CMD_Speed_Analysis(data)
        AgvCMDSpeed = (LeftCMDSpeed + RightCMDSpeed)/2
        return str(AgvCMDSpeed)
    except:
        print("AGV指令速度解析出错")


# ***************************************************************************************************#
# 解析小车实际速度，获取小车左右轮实际速度，再除以2得到小车实际速度
        
def Left_Real_Speed_Analysis(data):
    try:
        AGV_Left_Speed = data[44:48]  # 截取车辆左轮实际速度字段
        AGV_Left_Speed = int(AGV_Left_Speed, 16)
        AGV_Left_Speed_minus = AGV_Left_Speed & 32768
        if AGV_Left_Speed_minus != 0:
            AGV_Left_Speed = ((~AGV_Left_Speed) & 0xffff) + 1  # 等于1
            AGV_Left_Speed = AGV_Left_Speed * -1
        return str(AGV_Left_Speed)
    except:
        print("左轮实际速度解析出错")
####################################################################
def Right_Real_Speed_Analysis(data):
    try:
        AGV_Right_Speed = data[48:52]  # 截取车辆右轮实际速度字段
        AGV_Right_Speed = int(AGV_Right_Speed, 16)
        AGV_Right_Speed_minus = AGV_Right_Speed & 32768
        if AGV_Right_Speed_minus != 0:
            AGV_Right_Speed = ((~AGV_Right_Speed) & 0xffff) + 1  # 等于1
            AGV_Right_Speed = AGV_Right_Speed * -1
        
        return str(AGV_Right_Speed)
        #self.labelEdit_AgvSpeed.setText(str(((AGV_Left_Speed + AGV_Right_Speed) / 2) / 1000) + "m/s")  # 车辆速度
    except:
        print("右轮实际速度解析出错")
        
def AGV_Real_Speed(data):
    try:
        LeftSpeed = Left_Real_Speed_Analysis(data)
        RightSpeed =  Right_Real_Speed_Analysis(data)
        AgvSpeed = (LeftSpeed + RightSpeed)/2
        return str(AgvSpeed)
    except:
        print("AGV实际速度解析出错")
