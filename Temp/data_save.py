# ===========================
# 保存温度数据
# ===========================
def data_save(data):
    try:
        file = open('temp.txt', 'a')
        file.write(data)
        file.close()
    except:
        file.close()
