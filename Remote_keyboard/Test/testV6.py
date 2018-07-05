
import os
import shutil 

#对比文件（传入三个参数，分别是：templetFile-需要对比的文件，）
def CompareFile(filepath,templetFile,diffDir):
    templet = {}
    # 跳过一下序号
    exceptNum = [37,38,39, 51,60,72,73,74,79,100,101,102, 185]
    try:
        f = open(templetFile, 'r')
        templetlines = f.readlines()
        
        for line in templetlines:
            if('=' in line):
                key = line.split('=')
                num = int(key[0])
                param = key[1]
                tmpDict= {num:param}
                templet.update(tmpDict)
        f.close()  
        f = open(filepath, 'r')
        lines = f.readlines()
        
        for line in lines:
            if('=' in line):
                key = line.split('=')
                num = int(key[0])
                param = key[1]
                
                if (not num in exceptNum):
                    if(templet[num] != param):
                        fpath,fname = os.path.split(filepath)
                        if('/'in fpath):
                            name = fpath.split('/')
                        else:
                            name = fpath.split('\\')
                        if(not os.path.exists(diffDir)):
                            os.makedirs(diffDir)
                        shutil.copyfile(filepath, diffDir+'/'+name[len(name) -1 ])  
                        diffDir
        f.close()  

    except IOError:
        print("ERROR: 没有找到文件:%s或读取文件失败！" % filepath)
        exit(1)
        
#遍历目录文件
def CompareDir(curDir,templetFile,diffDir):
    # 判断目录存在
    if not os.path.isdir(curDir):   
        print ('这个函数是用来传送本地目录的')
        return
    # 遍历目录内容，上传资源
    for file in os.listdir(curDir):
        # 资源路径
        filepath = os.path.join(curDir, file) 

        # 判断资源文件类型
        if os.path.isfile(filepath): 
            # 1.文件
            CompareFile(filepath, templetFile,diffDir) 
        elif os.path.isdir(filepath):
            # 2.目录               
            CompareDir(filepath, templetFile,diffDir)
            
if __name__=="__main__":
    # =================================================================
    # 需要对比的文件存放路径
    #dir = 'C:/Users/kuaicanghwei/Desktop/无锡仓/params/116'
    # 将模板文件放在此路径下
    #templetFile = 'C:/Users/kuaicanghwei/Desktop/无锡仓/params/offlineslavesettings.properties'
    # 差异文件存放路径
    #diffDir = 'C:/Users/kuaicanghwei/Desktop/无锡仓/params/diff'
    # =================================================================
    
    # 需要对比的文件存放路径
    dir = 'params'
    # 将模板文件放在此路径下
    templetFile = './8001/offlineslavesettings.properties'
    # 差异文件存放路径
    diffDir = 'diff'
    CompareDir(dir,templetFile,diffDir)
