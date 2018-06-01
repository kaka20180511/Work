# ===============================
# 类的属性和方法的使用
# ===============================

class MyCounter:
    __secretCount = 0 # 私有变量
    publicCount = 0 # 公共变量
    
    def __privateCountFun(self):
        print("这是私有方法")
        self.__secretCount += 1
        self.publicCount +=1
        
    def publicCountFun(self):
        print("这是公共方法")
        self.__privateCountFun()
        
if __name__ == "__main__":
    counter = MyCounter()
    counter.publicCountFun()
    counter.publicCountFun()
    print("instance publicCount=%d" % counter.publicCount)
    #print("instance publicCount=%d" % MyCounter.publicCount)
    print("Class publicCount=%d"% MyCounter.publicCount)
    #print("Class publicCount=%d"% counter.__secretCount)
