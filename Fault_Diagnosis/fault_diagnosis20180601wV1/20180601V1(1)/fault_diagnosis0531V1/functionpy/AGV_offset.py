# ===============================
# 功能：解析AGVoffset值（x,y,heading）
# 2018/6/1 wm
# ==============================

# ===============================
# 解析AGVoffsetX数据并返回
def offset_x(data):
    try:
        offset_x_Hex = data[52:56]
        # 将十六进制转十进制
        offset_x_D = int(offset_x_Hex, 16)
        return str(offset_x_D)
        # 如果offsetX出现负数的情况下，将十六进制的负数数转换为十进制负数显示
        offset_x_D_minus = offset_x_D & 32768  # 用原码按位与的方法过滤掉正数，留下负数
        if offset_x_D_minus != 0:
            offset_x_D = ((~offset_x_D) & 0xffff) + 1  # 等于1
            offset_x_D = offset_x_D * -1
        return str(offset_x_D)
        
    except:
        print("解析offsetX出错")
# ===============================

# ===============================
# 解析AGVoffsetY数据并返回
def offset_y(data):
    try:
        offset_y_Hex = data[56:60]
        # 将十六进制转十进制
        offset_y_D = int(offset_y_Hex, 16)
        return str(offset_y_D)
        # 如果offsetY出现负数的情况下，将十六进制的负数数转换为十进制负数显示
        offset_y_D_minus = offset_y_D & 32768  # 用原码按位与的方法过滤掉正数，留下负数
        if offset_y_D_minus != 0:
            offset_y_D = ((~offset_y_D) & 0xffff) + 1  # 等于1
            offset_y_D = offset_y_D * -1
        return str(offset_y_D)
        
    except:
        print("解析offsetY出错")
# ===============================

# ===============================
# 解析AGVoffset_heading数据并返回（heading）
def offset_heading(data):
    try:
        offset_heading_Hex = data[60:64]
        # 将十六进制转十进制
        offset_heading_D = int(offset_heading_Hex, 16)
        # 如果offset_heading出现负数的情况下，将十六进制的负数数转换为十进制负数显示
        offset_heading_D_minus = offset_heading_D & 32768  # 用原码按位与的方法过滤掉正数，留下负数
        if offset_heading_D_minus != 0:
            offset_heading_D = ((~offset_heading_D) & 0xffff) + 1  # 等于1
            offset_heading_D = offset_heading_D * -1
        return str(offset_heading_D)
        
    except:
        print("解析offset_heading数据出错")
# ===============================
