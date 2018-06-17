import pygame

# Define some colors
# 定义一些颜色
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# 这是一个简单的课程，可以帮助我们打印到屏幕上
# It has nothing to do with the joysticks, just outputting the
# 它与游戏杆无关，只是输出
# information.
# 信息
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
# 设置屏幕的宽度和高度[宽度，高度]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
# 循环直到用户单击关闭按钮。
done = False

# Used to manage how fast the screen updates
# 用于管理屏幕更新速度
clock = pygame.time.Clock()

# Initialize the joysticks
# 初始化游戏杆
pygame.joystick.init()
    
# Get ready to print
# 准备好打印
textPrint = TextPrint()

# -------- Main Program Loop -----------
# -------- 主程序循环 -----------
while done==False:
    # EVENT PROCESSING STEP
    # 事件处理步骤 
    for event in pygame.event.get(): # User did something 用户做了些什么
        if event.type == pygame.QUIT: # If user clicked close 如果用户点击关闭
            done=True # Flag that we are done so we exit this loop 标记我们已完成，因此我们退出此循环
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        # 可能的操纵杆动作: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            # 操纵杆按钮被按下
            print("Joystick button pressed.")
            
        if event.type == pygame.JOYBUTTONUP:
            # 操纵杆按钮释放
            print("Joystick button released.")
            
 
    # DRAWING STEP
    # 绘图步骤
    # First, clear the screen to white. Don't put other drawing commands
    # 首先，将屏幕清除为白色。 不要放其他绘图命令
    # above this, or they will be erased with this command.
    # 在此之上，或者它们将被删除这个命令。
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    # 获取游戏杆的数量
    joystick_count = pygame.joystick.get_count()
    # 游戏杆数量
    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    
    # For each joystick:
    # 对于每个游戏杆
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.print(screen, "Joystick {}".format(i) )
        textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        # 从操作系统获取控制器/操纵杆的名称
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # 通常轴成对地运行，上/下一个，左/右另一个
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes) )
        textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        textPrint.unindent()
            
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        textPrint.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # 帽子开关。 方向的全部或全部没有，不像游戏杆。
        # Value comes back in an array.
        # 值返回到一个数组中。
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats) )
        textPrint.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
        textPrint.unindent()
        
        textPrint.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    # 所有代码绘制应该超出本评论
    # Go ahead and update the screen with what we've drawn.
    # 继续并使用我们绘制的内容更新屏幕。
    pygame.display.flip()

    # Limit to 20 frames per second
    # 限于每秒20帧
    clock.tick(20)
    
# Close the window and quit.
# 关闭窗口并退出
# If you forget this line, the program will 'hang'
# 如果你忘记这一行，程序将'挂起'
# on exit if running from IDLE.
# 退出时如果从IDLE运行。
pygame.quit ()
