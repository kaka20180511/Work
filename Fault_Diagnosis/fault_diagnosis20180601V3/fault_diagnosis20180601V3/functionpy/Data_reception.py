# ===============================
# 功能：解析AGV坐标数据（x,y,车头角度）
# 2018/6/1 lsl
# ===============================

# ===============================
# 解析AGV坐标x数据并返回
def coordinate_x(data):
    try:
        coordinate_x_Hex = data[6:14]
        # 将十六进制转十进制
        coordinate_x_D = int(coordinate_x_Hex, 16)
        return str(coordinate_x_D)
        
    except:
        print("解析AGV坐标数据出错")
# ===============================

# ===============================
# 解析AGV坐标y数据并返回
def coordinate_y(data):
    try:
        coordinate_y_Hex = data[14:22]
        # 将十六进制转十进制
        coordinate_y_D = int(coordinate_y_Hex, 16)
        return str(coordinate_y_D)
        
    except:
        print("解析AGV坐标数据出错")
# ===============================

# ===============================
# 解析AGV坐标角度数据并返回（heading）
def coordinate_heading(data):
    try:
        coordinate_heading_Hex = data[22:26]
        # 将十六进制转十进制
        coordinate_heading_D = int(coordinate_heading_Hex, 16)
        # 如果车辆角度出现负数的情况下，将十六进制的负数数转换为十进制负数显示
        coordinate_heading_D_minus = coordinate_heading_D & 32768  # 用原码按位与的方法过滤掉正数，留下负数
        if coordinate_heading_D_minus != 0:
            coordinate_heading_D = ((~coordinate_heading_D) & 0xffff) + 1  # 等于1
            coordinate_heading_D = coordinate_heading_D * -1
        return str(coordinate_heading_D)
        
    except:
        print("解析AGV坐标角度数据出错")
# ===============================
