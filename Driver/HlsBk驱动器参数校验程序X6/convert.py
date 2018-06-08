import binascii
out = str("fffffffffffffffff")

team1 = binascii.b2a_hex(out)#ASCII码转换成16进制数据
team2 = team1.decode('utf-8')#将bytes类型转换成str型
#print(team2[6:10])
team3 = team2[6:10]#分片提取温度
#print(team3)
team4 = int(team3,16)#16进制转10进制
print(team4)
