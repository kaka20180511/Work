
# 用于检测在窗口中输入设备的动作
# 包括键盘键值，鼠标点击移动等动作

import pygame
import sys

# 初始化pygame
pygame.init()

size = width, height = 600, 400  # 设置窗口大小，size实际为元组
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Demo")  # 窗口标题
bg = (0, 0, 0)  # 背景填充颜色

font = pygame.font.Font(None, 20)  # 字体None使用系统默认字体，大小为20
line_height = font.get_linesize()  # 获取字体文本的行高
position = 0

screen.fill(bg)  # 填充背景色

while True:
    for event in pygame.event.get():  # 从队列中获取事件
        if event.type == pygame.QUIT:  # 判断是否点击退出动作
            sys.exit()
            
        print(event.type)

        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))  # 在面板上绘制事件文本，绿色
        position += line_height  # 切换到下一行显示

        if position > height:  # 下一页显示
            position = 0
            screen.fill(bg)

    pygame.display.flip()  # 更新整个面板显示在屏幕上
