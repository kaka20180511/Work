# ===============================
# 功能：解析车辆运动状态并返回给主函数
# （需要分正常帧和特殊帧，正常帧为车辆
# 运动状态，特殊帧为电量和版本号是否有
# 效标志位
# 2018/06/01  lsl
# ===============================

# ===============================
# 解析车辆运动状态(normal_frame_motionstatus)
def normal_frame_motionstatus(data):
    try:
        AGV_Kinestate = data[26:28]  # 截取车辆运动状态字段
        AGV_Kinestate = int(AGV_Kinestate, 16)
        if AGV_Kinestate == 0:
            sMotionStatus = "停止"

        if AGV_Kinestate == 1:
            sMotionStatus = "旋转"

        if AGV_Kinestate == 2:
            sMotionStatus = "顶升"

        if AGV_Kinestate == 3:
            sMotionStatus = "下降"

        if AGV_Kinestate == 4:
            sMotionStatus = "移动"

        if AGV_Kinestate == 5:
            sMotionStatus = "暂停"

        if AGV_Kinestate == 8:
           sMotionStatus = "托盘回零位"

        if AGV_Kinestate == 9:
            sMotionStatus = "托盘碰限位"

        if AGV_Kinestate == 11:
           sMotionStatus = "软停"

        if AGV_Kinestate == 12:
            sMotionStatus = "货架换向"

        if AGV_Kinestate == 14:
            sMotionStatus = "托盘寸动"

        if AGV_Kinestate == 15:
            sMotionStatus = "陀螺仪零偏"

        if AGV_Kinestate == 16:
            sMotionStatus = "微移动"

        if AGV_Kinestate == 19:
            sMotionStatus = "顶升前打开上置摄像头"

        if AGV_Kinestate == 20:
            sMotionStatus == "顶升后打开上置摄像头"

        if AGV_Kinestate == 21:
            sMotionStatus = "获取下位机版本"

        if AGV_Kinestate == 22:
            sMotionStatus = "退出充电"

        if AGV_Kinestate == 23:
            sMotionStatus = "跟车"

        if AGV_Kinestate == 24:
            sMotionStatus = "顶升后确认"
        return sMotionStatus
    except:
        print("解析车辆运动状态出错")   
# ===============================

# ===============================
# 解析车辆状态上传数据有效位（bit0：参
# 数帧、位置偏差、电量显示、上置摄像头
# 信息、版本号、里程、路径规划信息,及指
# 令速度异常信息、负载率是否上传）
def special_frame_motionstatus(data):
    pass
