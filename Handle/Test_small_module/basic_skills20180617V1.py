# =============================
# 功能：获取手柄操作数据（罗技F710）
# 2018/06/17 lsl
# =============================
import time
import pygame

pygame.display.init()
# 
pygame.joystick.init()
# 初始化操作杆 
pygame.joystick.Joystick(0).init()

# Get the name of the joystick and print it
# 获取操纵杆的名称并打印出来
JoyName = pygame.joystick.Joystick(0).get_name()
print ("Name of the joystick:")
print (JoyName)

# Get the number of axes
# 获取轴的数量
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print ("Number of axis:")
print (JoyAx)
# 获取按键的数量
Joybuttons = pygame.joystick.Joystick(0).get_numbuttons()
print (Joybuttons)

# 获取键帽的数量
Joyhats = pygame.joystick.Joystick(0).get_numhats()
print (Joyhats)

while True:
    pygame.event.pump()
    # ==========================================
    # 功能：获取手柄按键数据并打印
    # 打印X按钮状态
    print (pygame.joystick.Joystick(0).get_button(0))
    # 打印A按钮状态 
    print (pygame.joystick.Joystick(0).get_button(1))
    # 打印B按钮状态 
    print (pygame.joystick.Joystick(0).get_button(2))
    # 打印Y按钮状态 
    print (pygame.joystick.Joystick(0).get_button(3))
    # 打印LB按钮状态
    print (pygame.joystick.Joystick(0).get_button(4))
    # 打印RB按钮状态
    print (pygame.joystick.Joystick(0).get_button(5))   
    # 打印LT按钮状态
    print (pygame.joystick.Joystick(0).get_button(6))  
    # 打印RT按钮状态
    print (pygame.joystick.Joystick(0).get_button(7))  
    # 打印BACK按钮状态
    print (pygame.joystick.Joystick(0).get_button(8)) 
    # 打印START按钮状态
    print (pygame.joystick.Joystick(0).get_button(9)) 
    # 打印左摇杆按钮状态（左右摇杆是可以按下的）
    print (pygame.joystick.Joystick(0).get_button(10)) 
    # 打印右摇杆按钮状态（左右摇杆是可以按下的）
    print (pygame.joystick.Joystick(0).get_button(11)) 
    # ==========================================
    
    # ==========================================
    # 功能：打印获得摇杆操作轴的当前坐标
    # 打印左摇杆状态 
    print (pygame.joystick.Joystick(0).get_axis(1))
    # 打印右摇杆状态 
    print (pygame.joystick.Joystick(0).get_axis(2))
    # ==========================================
    
    # ==========================================
    # 功能：打印获得键帽的当前按键状态（注：键帽是返回数组）    
    print (pygame.joystick.Joystick(0).get_hat(0))
    # ==========================================
    time.sleep(0.1)

