# =================================================
# 处理从串口读到的数据
# =================================================
import binascii    # 加载ascii模块
import time
def data_reduction(data):
    team1 = binascii.b2a_hex(data)
    team2 = team1.decode('utf-8')
    team3 = team2[6:10]
    print(team3)
    team4 = int(team3, 16)
    curtime = time.strftime("%H:%M:%S", time.localtime())
    team5 = curtime + '   ' + str(team4 / 10) + '℃' + '\n'
    return team5
