# ===============================
# 功能：解析车辆托盘角度数据并返回给主
# 函数（正常帧为托盘数据、特殊帧为电量
# 数据）
# 2018/05/31  lsl
# ===============================

# ===============================
# 功能：解析正常帧（托盘角度podspeed）
# 28-32字段
def PodAngle(data):
    try:
        AGV_PodAngle = data[28:32]  # 截取车辆托盘角度字段
        AGV_PodAngle = int(AGV_PodAngle, 16)
        AGV_PodAngle_minus = AGV_PodAngle & 32768
        if AGV_PodAngle_minus != 0:
            AGV_PodAngle = ((~AGV_PodAngle) & 0xffff) + 1  # 等于1
            AGV_PodAngle = AGV_PodAngle * -1
        else:
            AGV_PodAngle = AGV_PodAngle - 18000
        return str(AGV_PodAngle)
        
    except:
        pass
# ===============================
