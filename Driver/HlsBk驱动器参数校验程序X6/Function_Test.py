import sys
def One_test():
    z = 10
    while(z):
        z = z-1
        print("第一个函数")
def Two_test():
    z = 10
    while(z):
        z = z-1
        print("第二个函数")
        


x1 = input("请输入")
x2 = int(x1)
if x2 == 1:
    One_test()
    
if x2 == 2:
    Two_test()



