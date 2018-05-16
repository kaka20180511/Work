# ==================================
# 重命名文件
# ==================================
import os
import time
def file_rename():
    try:
        curtime_last = str(time.strftime("%Y %m %d %H %M %S ", time.localtime())) + ".txt"
        os.rename("temp.txt",curtime_last)
        #print(curtime_last)
    except:
        pass
#file_rename()
