"""
功能：读取驱动器查询命令文件并返回命令列表
"""
import xlrd  # 导入模块
import binascii

x = 0  # 配置读取命令表的起始行
def Data_Read(file):
    data = xlrd.open_workbook(file)  # 打开文件
    table = data.sheets()[0]  # 通过索引顺序获取一个工作表
    Rxd = table.cell(x, 1).value  # 获取第2行第2列这个位置的数据
    # print(Rxd)
    a = str(Rxd)
    a_list = []
    for i in a.split():  # 拆分字符串
        a_list.append(binascii.a2b_hex(i))
    return a_list
