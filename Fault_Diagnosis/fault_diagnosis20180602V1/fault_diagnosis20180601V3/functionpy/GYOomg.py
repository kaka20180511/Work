# ===============================
# 功能：解析正常帧中车辆陀螺角速度并返
# 回给主函，特殊帧暂时未做
# 2018/05/31  lsl
# ===============================

# ===============================
# 解析正常帧中陀螺仪角速度（32:36）
def GYOomg(data):
    try:
        AGV_GYOomg_Hex = data[32:36]
        # 将十六进制转十进制
        AGV_GYOomg_Hex_D = int(AGV_GYOomg_Hex, 16)
        # 如果车辆角度出现负数的情况下，将十六进制的负数数转换为十进制负数显示
        AGV_GYOomg_Hex_D_minus = AGV_GYOomg_Hex_D & 32768  # 用原码按位与的方法过滤掉正数，留下负数
        if AGV_GYOomg_Hex_D_minus != 0:
            AGV_GYOomg_Hex_D = ((~AGV_GYOomg_Hex_D) & 0xffff) + 1  # 等于1
            AGV_GYOomg_Hex_D = AGV_GYOomg_Hex_D * -1
        return AGV_GYOomg_Hex_D
        
    except:
        print("解析AGV坐标角度数据出错")
# ===============================

