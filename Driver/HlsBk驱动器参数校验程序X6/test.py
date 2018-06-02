"""
功能：计算文本行数
"""
filename = "123.txt"
myfile = open(filename) 
lines = len(myfile.readlines()) 
print (lines)
