# ==========================================
# 功能：小车诊断工具
# 2018-05-28 longshenglin
# ==========================================
import sys
import random
import threading
import time
import serial
import binascii
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

from functionpy.motor_data import *
from functionpy.AGV_offset import *
from functionpy.GYOomg import *
from functionpy.pod_speed import *
from functionpy.AGV_motionstatus import *
from functionpy.Data_reception import *
from functionpy.AGV_cmd_state import *
from functionpy.AGV_state import *
#from Ui_Move_Dialog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QInputDialog
from functionpy.Ui_Main_Ui_Fault_Diagnosis import Ui_MainWindow

# =======================================================
# 设置一个全局变量用于串口的调用
ser = serial.Serial(port="COM2",
                    baudrate=38400,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=0.1
                    )
# =======================================================

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 实例化Sun类
        self.sum = Sum()
        # 将信号连接到printNum函数
        self.sum.sinOut.connect(self.decode)
        # 开启线程
        self.sum.start()
    
    # ==========================================
    # 功能：将每一帧数据添加到界面原始数据框里
    # 并开始解析
    def decode(self, num):
        #print(num)
        self.textEdit_data_show.append(num)  # 显示原始数据
        # ==========================================
        # 功能：将AGV的命令执行状态在UI上显示（颜色不同）
        self.label_Command_Mode.setText(status_cmd(num))
        if status_cmd(num) == "命令执行完成":
            self.label_Command_Mode.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
                    
        if status_cmd(num) == "命令执行中":
            self.label_Command_Mode.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(255, 185, 15)")  # 设置边框宽度和颜色；设置字体颜色
                    
        if status_cmd(num) == "接收到错误指令":
            self.label_Command_Mode.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);")  # 设置边框宽度和颜色；设置字体颜色
                    
        if status_cmd(num) == "指令因错误而终止":
            self.label_Command_Mode.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
        #print(status_cmd(num))           
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的托盘限位状态在UI上显示（颜色不同）
        self.label_salver.setText(status_ls(num))
        if status_ls(num) == "托盘限位未确认":
             self.label_salver.setStyleSheet("border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
            
        if status_ls(num) == "托盘限位已确认":
            self.label_salver.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
    
        #print(status_ls(num))           
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的陀螺仪状态在UI上显示（颜色不同）
        self.label_gyroscope.setText(status_gyrozero(num))
        if status_gyrozero(num) == "陀螺零偏纠正中":
             self.label_gyroscope.setStyleSheet("border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
            
        if status_gyrozero(num) == "陀螺零偏纠正完成":
            self.label_gyroscope.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
    
        #print(status_gyrozero(num))           
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的货架状态状态在UI上显示（颜色不同）
        self.label_shelves.setText(status_bucket(num))
        if status_bucket(num) == "没带货架":
             self.label_shelves.setStyleSheet("border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
            
        if status_bucket(num) == "带货架":
            self.label_shelves.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
                    
        if status_bucket(num) == "不确定":
            self.label_shelves.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);")  # 设置边框宽度和颜色；设置字体颜色
    
        #print(status_bucket(num))           
        # ==========================================
        # ==========================================
        # 功能：将AGV的下视读码状态在UI上显示（颜色不同）
        self.label_code.setText(status_barcode(num))
        if status_barcode(num) == "不在码上":
             self.label_code.setStyleSheet("border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
            
        if status_barcode(num) == "在码上":
            self.label_code.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
    
        #print(status_barcode(num))           
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的电机状态在UI上显示（颜色不同）
        self.label_Motor_switch.setText(status_motorenable(num))
        if status_motorenable(num) == "电机关闭":
             self.label_Motor_switch.setStyleSheet("border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
            
        if status_motorenable(num) == "电机打开":
            self.label_Motor_switch.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
    
        #print(status_barcode(num))           
        # ==========================================
        # ==========================================
        # 调用函数返回命令ID
        # 打印命令ID
        print(cmd_ID(num))
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的数据帧状态在UI上显示（颜色不同）
        self.label_13.setText(data_frame(num))
        if data_frame(num) == "特殊帧":
             self.label_13.setStyleSheet("border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
            
        if data_frame(num) == "正常帧":
            self.label_13.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
    
        #print(data_frame(num))           
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的运行状态在UI上显示（颜色不同）
        self.label_18.setText(sleepFlag(num))
        if sleepFlag(num) == "休眠":
             self.label_18.setStyleSheet("border: 1px solid rgb(36, 36, 36);color: rgb(205, 38, 38)")  # 设置边框宽度和颜色；设置字体颜色
            
        if sleepFlag(num) == "运行":
            self.label_18.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
    
        #print(sleepFlag(num))           
        # ==========================================
        # ==========================================
        # 调用函数返回命令摄像头状态        
        print(CameraDataValid(num)) 
        # ==========================================
        # ==========================================
        # 调用函数返回AGV运行状态        
        print(RunMode(num)) 
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的x坐标数据在UI上显示（颜色不同）
        self.labelEdit_DSP_X.setText(coordinate_x(num))
        self.labelEdit_DSP_X.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色        
        # ==========================================

        # ==========================================
        # 功能：将AGV的y坐标数据在UI上显示（颜色不同）
        self.labelEdit_DSP_Y.setText(coordinate_y(num))
        self.labelEdit_DSP_Y.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色        
        # ==========================================

        # ==========================================
        # 功能：将AGV的角度坐标数据在UI上显示（颜色不同）
        self.labelEdit_DSP_H.setText(coordinate_heading(num))
        self.labelEdit_DSP_H.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色        
        # ==========================================
        
        # ==========================================
        # 功能：将AGV的运动状态在UI上显示
        #print(normal_frame_motionstatus(num))
        self.labelEdit_MotionStatus.setText(normal_frame_motionstatus(num))
        self.labelEdit_MotionStatus.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色   
        # ==========================================

        # ==========================================
        # 功能：将AGV的托盘角度在UI上显示
        self.labelEdit_PodaAngle.setText(PodAngle(num))
        self.labelEdit_PodaAngle.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色   
        # ==========================================
                    
        # ==========================================
        # 功能：将AGV的陀螺角速度在UI上显示
        print(GYOomg(num))
        # ==========================================
        # ==========================================
        # 功能：将小车左侧指令速度数据在UI上显示
        print(Left_CMD_Speed_Analysis(num))
        
        # ==========================================
        
        # ==========================================
        # 功能：将小车右侧指令速度数据在UI上显示
        print(Right_CMD_Speed_Analysis(num))
        
        # ==========================================
        
        # ==========================================
        # 功能：将小车速度数据在UI上显示
        self.labelEdit_AgvSpeed.setText(AGV_Real_Speed(num))
        self.labelEdit_AgvSpeed.setStyleSheet(
                    "border: 1px solid rgb(36, 36, 36);color: rgb(30, 144, 255)")  # 设置边框宽度和颜色；设置字体颜色
        # ==========================================
        
        # ==========================================
        # 功能：将AGV x方向偏差在UI上显示
        print(offset_x(num))
        # ==========================================
        # ==========================================
        # 功能：将AGV y方向偏差在UI上显示
        print(offset_y(num))
        
        # ==========================================
        
        # ==========================================
        # 功能：将AGV 角度偏差在UI上显示
        print(offset_heading(num))
        
        # ==========================================
        
    # ==========================================

    # ==========================================
    # 功能：读取用户选择转换命令为脚本并加载到文本框内
    # ==========================================
    @pyqtSlot()
    def on_pushButton_Add_Cmd_clicked(self):

        # ==========================================
        # 功能：加载循环次数对话框
        def loop_times():
            # 建立对话框
            dialog = QDialog()
            # 设置窗口主题颜色
            dialog.setStyleSheet("    color: #eff0f1;\n"
                                 "    background-color: #31363b;\n"
                                 "    selection-background-color:#3daee9;\n"
                                 "    selection-color: #eff0f1;\n"
                                 "    background-clip: border;\n"
                                 "    border-image: none;\n"
                                 "    outline: 0;")
            dialog.setWindowTitle("请输入目循环次数：")
            # 设置窗口大小
            dialog.resize(220, 155)
            # 添加一个标签
            label = QLabel(dialog)
            label.setText("角度：")
            label.resize(55, 15)
            label.move(30, 52)

            # 添加一个单行文本框
            lineEdit = QLineEdit(dialog)
            lineEdit.resize(110, 20)
            lineEdit.move(80, 50)
            lineEdit.setInputMask("999999")

            def Determine_loop():
                input_loop = lineEdit.text()
                print(input_loop)

                # 处理用户不输入数据的情况
                if input_loop == "":
                    input_loop = "1"

                Script_loop = "loop" + " " + str(input_loop)
                self.textEdit.append(Script_loop)
                dialog.close()
                pass

            # 关闭按钮逻辑子函数
            def close_dialog():
                # print("关闭按钮被按下！")
                dialog.close()

            # 增加确定按钮
            button_determine = QPushButton("确定", dialog)
            button_determine.resize(75, 25)
            button_determine.move(20, 110)
            button_determine.clicked.connect(Determine_loop)

            # 增加取消按钮
            button_cancel = QPushButton("取消", dialog)
            button_cancel.resize(75, 25)
            button_cancel.move(120, 110)
            button_cancel.clicked.connect(close_dialog)

            # 初始化对话框
            dialog.setWindowModality(Qt.NonModal)
            dialog.exec_()
        # ==========================================

        # ==========================================
        # 功能：加载移动对话框
        def move_cmd():
            dialog = QDialog()  # 建立弹出对话框
            # 设置窗口主题颜色
            dialog.setStyleSheet("    color: #eff0f1;\n"
                                 "    background-color: #31363b;\n"
                                 "    selection-background-color:#3daee9;\n"
                                 "    selection-color: #eff0f1;\n"
                                 "    background-clip: border;\n"
                                 "    border-image: none;\n"
                                 "    outline: 0;")
            dialog.setWindowTitle("请输入目标点坐标")
            dialog.resize(220, 155)  # 设置窗口大小
            # 添加一个标签1
            label = QLabel(dialog)
            label.setText("X坐标值： ")
            label.resize(55, 15)
            label.move(20, 30)

            # 添加一个标签2
            labe2 = QLabel(dialog)
            labe2.setText("Y坐标值： ")
            labe2.resize(55, 15)
            labe2.move(20, 70)

            # 添加一个单行文本输入框1
            lineEdit = QLineEdit(dialog)
            lineEdit.resize(110, 20)
            lineEdit.move(80, 30)
            lineEdit.setInputMask("999999")  # 限制用户输入，9为限制用户只能输入数字

            # 添加一个单行文本输入框1
            lineEdit2 = QLineEdit(dialog)
            lineEdit2.resize(110, 20)
            lineEdit2.move(80, 70)
            lineEdit2.setInputMask("999999")

            # 确定按钮逻辑子函数
            def Determine_move():
                # 获取用户输入的X坐标
                input_move_X = lineEdit.text()
                input_move_Y = lineEdit2.text()
                print("X坐标值：", input_move_X)
                print("Y坐标值：", input_move_Y)
                # 处理用户不输入数据
                if input_move_X == "":
                    input_move_X = "0000"

                if input_move_Y == "":
                    input_move_Y = "0000"

                x = input_move_X
                y = input_move_Y
                Script = "move" + " " + str(x) + " " + str(y)
                self.textEdit.append(Script)  # 显示原始数据
                dialog.close()

            # 关闭按钮逻辑子函数
            def close_dialog():
                # print("关闭按钮被按下！")
                dialog.close()

            # 添加一个确定按钮
            btn1 = QPushButton("确定", dialog)  # 创建一个按钮
            btn1.resize(75, 25)  # 设置按钮大小
            btn1.move(20, 110)
            btn1.clicked.connect(Determine_move)

            # 添加一个取消按钮
            btn2 = QPushButton("取消", dialog)  # 创建一个按钮
            btn2.resize(75, 25)  # 设置按钮大小
            btn2.move(120, 110)
            btn2.clicked.connect(close_dialog)
            dialog.setWindowModality(Qt.NonModal)
            dialog.exec_()
        # ==========================================

        # ==========================================
        # 旋转
        def Rotating_cmd():
            dialog = QDialog()  # 建立弹出对话框
            # 设置窗口主题颜色
            dialog.setStyleSheet("    color: #eff0f1;\n"
                                 "    background-color: #31363b;\n"
                                 "    selection-background-color:#3daee9;\n"
                                 "    selection-color: #eff0f1;\n"
                                 "    background-clip: border;\n"
                                 "    border-image: none;\n"
                                 "    outline: 0;")
            dialog.setWindowTitle("请输入目标角度")
            dialog.resize(220, 155)  # 设置窗口大小
            # 添加一个标签1
            label = QLabel(dialog)
            label.setText("目标角度： ")
            label.resize(55, 15)
            label.move(20, 30)

            # 添加一个单行文本输入框1
            lineEdit = QLineEdit(dialog)
            lineEdit.resize(110, 20)
            lineEdit.move(80, 30)
            lineEdit.setInputMask("999999")  # 限制用户输入，9为限制用户只能输入数字

            # 转向脚本逻辑子函数
            def Determine():
                # 获取用户输入的X坐标
                input_move_lifting = lineEdit.text()
                print("目标角度值：", input_move_lifting)
                # 处理用户不输入数据
                if input_move_lifting == "":
                    input_move_lifting = "0000"

                lift = input_move_lifting

                Script = "rotate" + " " + str(lift)  # 文本框中的
                self.textEdit.append(Script)  # 显示原始数据
                dialog.close()


                # ==========================================
                # 功能：加载转向命令的按钮

            # 关闭按钮逻辑子函数
            def close_1():
                # print("关闭按钮被按下！")
                dialog.close()

            # 添加一个确定按钮
            btn1 = QPushButton("确定", dialog)  # 创建一个按钮
            btn1.resize(75, 25)  # 设置按钮大小
            btn1.move(20, 110)
            btn1.clicked.connect(Determine)

            # 添加一个取消按钮
            btn2 = QPushButton("取消", dialog)  # 创建一个按钮
            btn2.resize(75, 25)  # 设置按钮大小
            btn2.move(120, 110)
            btn2.clicked.connect(close_1)

            dialog.setWindowModality(Qt.NonModal)
            dialog.exec_()
        # ==========================================

        # ==========================================
        # 功能：加载顶升对话框 author：zzp
        def Lifting_cmd():
            dialog = QDialog()  # 建立弹出对话框
            # 设置窗口主题颜色
            dialog.setStyleSheet("    color: #eff0f1;\n"
                                 "    background-color: #31363b;\n"
                                 "    selection-background-color:#3daee9;\n"
                                 "    selection-color: #eff0f1;\n"
                                 "    background-clip: border;\n"
                                 "    border-image: none;\n"
                                 "    outline: 0;")
            dialog.setWindowTitle("请输入目标角度")
            dialog.resize(220, 155)  # 设置窗口大小
            # 添加一个标签1
            label = QLabel(dialog)
            label.setText("角度： ")
            label.resize(55, 15)
            label.move(20, 30)

            # 添加一个单行文本输入框1
            lineEdit = QLineEdit(dialog)
            lineEdit.resize(110, 20)
            lineEdit.move(80, 30)
            lineEdit.setInputMask("999999")  # 限制用户输入，9为限制用户只能输入数字

            # 顶升脚本逻辑子函数
            def Determine():
                # 获取用户输入的X坐标
                input_move_lifting = lineEdit.text()
                print("目标高度值：", input_move_lifting)
                # 处理用户不输入数据
                if input_move_lifting == "":
                    input_move_lifting = "0000"

                lift = input_move_lifting

                Script = "liftup" + " " + str(lift)  # 文本框中的
                self.textEdit.append(Script)  # 显示原始数据
                dialog.close()

                # ==========================================
                # 功能：加载顶升命令的按钮

            # 关闭按钮逻辑子函数
            def close_1():
                # print("关闭按钮被按下！")
                dialog.close()

            # 添加一个确定按钮
            btn1 = QPushButton("确定", dialog)  # 创建一个按钮
            btn1.resize(75, 25)  # 设置按钮大小
            btn1.move(20, 110)
            btn1.clicked.connect(Determine)

            # 添加一个取消按钮
            btn2 = QPushButton("取消", dialog)  # 创建一个按钮
            btn2.resize(75, 25)  # 设置按钮大小
            btn2.move(120, 110)
            btn2.clicked.connect(close_1)

            dialog.setWindowModality(Qt.NonModal)
            dialog.exec_()
        # ==========================================

        # ==========================================
        # 功能：加载降下命令
        def down_cmd():
            dialog_down = QDialog()
            dialog_down.setStyleSheet(" color: #eff0f1;\n"
                                      "    background-color: #31363b;\n"
                                      "    selection-background-color:#3daee9;\n"
                                      "    selection-color: #eff0f1;\n"
                                      "    background-clip: border;\n"
                                      "    border-image: none;\n"
                                      "    outline: 0;")
            dialog_down.setWindowTitle("请输入目标角度")
            dialog_down.resize(220, 155)
            label = QLabel(dialog_down)
            label.setText("角度：")
            label.resize(55, 15)
            label.move(30, 52)

            lineEdit = QLineEdit(dialog_down)
            lineEdit.resize(110, 20)
            lineEdit.move(80, 50)
            # 限制用户只能输入0-9之间的数字
            lineEdit.setInputMask("999999")

            # 转换下降按钮函数
            def Determine_down():
                input_down = lineEdit.text()

                # 处理用户不输入数据的情况
                if input_down == "":
                    input_down = "0"

                Script_down = "putdown" + " " + str(input_down)

                # 将转换好的命令写入多行文本框
                self.textEdit.append(Script_down)

                # 关闭对话框
                dialog_down.close()
                pass

            def close_dialog_down():
                dialog_down.close()

            # 增加确定按钮
            button_determine = QPushButton("确定", dialog_down)
            button_determine.resize(75, 25)
            button_determine.move(20, 110)
            button_determine.clicked.connect(Determine_down)

            # 增加取消按钮
            button_cancel = QPushButton("取消", dialog_down)
            button_cancel.resize(75, 25)
            button_cancel.move(120, 110)
            button_cancel.clicked.connect(close_dialog_down)

            # 初始化对话框
            dialog_down.setWindowModality(Qt.NonModal)
            dialog_down.exec_()
        # ==========================================

        # ==========================================
        # 充电
        def Charging_cmd():
            dialog = QDialog()  # 建立弹出对话框
            # 设置窗口主题颜色
            dialog.setStyleSheet("    color: #eff0f1;\n"
                                 "    background-color: #31363b;\n"
                                 "    selection-background-color:#3daee9;\n"
                                 "    selection-color: #eff0f1;\n"
                                 "    background-clip: border;\n"
                                 "    border-image: none;\n"
                                 "    outline: 0;")
            dialog.setWindowTitle("请输入目标点坐标")
            dialog.resize(220, 155)  # 设置窗口大小
            # 添加一个标签1
            label = QLabel(dialog)
            label.setText("X坐标值： ")
            label.resize(55, 15)
            label.move(20, 30)

            # 添加一个标签2
            labe2 = QLabel(dialog)
            labe2.setText("Y坐标值： ")
            labe2.resize(55, 15)
            labe2.move(20, 70)

            # 添加一个单行文本输入框1
            lineEdit = QLineEdit(dialog)
            lineEdit.resize(110, 20)
            lineEdit.move(80, 30)
            lineEdit.setInputMask("999999")  # 限制用户输入，9为限制用户只能输入数字

            # 添加一个单行文本输入框1
            lineEdit2 = QLineEdit(dialog)
            lineEdit2.resize(110, 20)
            lineEdit2.move(80, 70)
            lineEdit2.setInputMask("999999")

            # 充电脚本逻辑子函数
            def Determine():
                # 获取用户输入的X坐标
                input_move_X = lineEdit.text()
                input_move_Y = lineEdit2.text()
                print("X坐标值：", input_move_X)
                print("Y坐标值：", input_move_Y)
                # 处理用户不输入数据
                if input_move_X == "":
                    input_move_X = "0000"

                if input_move_Y == "":
                    input_move_Y = "0000"

                x = input_move_X
                y = input_move_Y
                Script = "charge" + " " + str(x) + " " + str(y)
                self.textEdit.append(Script)  # 显示原始数据
                dialog.close()

                # ==========================================
                # 功能：加载移动命令的按钮  

            # 关闭按钮逻辑子函数
            def close_1():
                # print("关闭按钮被按下！")
                dialog.close()

            # 添加一个确定按钮
            btn1 = QPushButton("确定", dialog)  # 创建一个按钮
            btn1.resize(75, 25)  # 设置按钮大小
            btn1.move(20, 110)
            btn1.clicked.connect(Determine)

            # 添加一个取消按钮
            btn2 = QPushButton("取消", dialog)  # 创建一个按钮
            btn2.resize(75, 25)  # 设置按钮大小
            btn2.move(120, 110)
            btn2.clicked.connect(close_1)

            dialog.setWindowModality(Qt.NonModal)
            dialog.exec_()
        # ==========================================

        def Exitcharge_cmd():
            dialog = QDialog()  # 建立弹出对话框
            # 设置窗口主题颜色
            dialog.setStyleSheet("    color: #eff0f1;\n"
                                 "    background-color: #31363b;\n"
                                 "    selection-background-color:#3daee9;\n"
                                 "    selection-color: #eff0f1;\n"
                                 "    background-clip: border;\n"
                                 "    border-image: none;\n"
                                 "    outline: 0;")
            dialog.setWindowTitle("请输入目标点坐标")
            dialog.resize(220, 155)  # 设置窗口大小
            # 添加一个标签1
            label = QLabel(dialog)
            label.setText("X坐标值： ")
            label.resize(55, 15)
            label.move(20, 30)

            # 添加一个标签2
            labe2 = QLabel(dialog)
            labe2.setText("Y坐标值： ")
            labe2.resize(55, 15)
            labe2.move(20, 70)

            # 添加一个单行文本输入框1
            lineEdit = QLineEdit(dialog)
            lineEdit.resize(110, 20)
            lineEdit.move(80, 30)
            lineEdit.setInputMask("999999")  # 限制用户输入，9为限制用户只能输入数字

            # 添加一个单行文本输入框1
            lineEdit2 = QLineEdit(dialog)
            lineEdit2.resize(110, 20)
            lineEdit2.move(80, 70)
            lineEdit2.setInputMask("999999")

            # 充电脚本逻辑子函数
            def Determine():
                # 获取用户输入的X坐标
                input_move_X = lineEdit.text()
                input_move_Y = lineEdit2.text()
                print("X坐标值：", input_move_X)
                print("Y坐标值：", input_move_Y)
                # 处理用户不输入数据
                if input_move_X == "":
                    input_move_X = "0000"

                if input_move_Y == "":
                    input_move_Y = "0000"

                x = input_move_X
                y = input_move_Y
                Script = "exitcharge" + " " + str(x) + " " + str(y)
                self.textEdit.append(Script)  # 显示原始数据
                dialog.close()

            # ==========================================
            # 功能：加载移动命令的按钮

            # 关闭按钮逻辑子函数
            def close_1():
                # print("关闭按钮被按下！")
                dialog.close()

            # 添加一个确定按钮
            btn1 = QPushButton("确定", dialog)  # 创建一个按钮
            btn1.resize(75, 25)  # 设置按钮大小
            btn1.move(20, 110)
            btn1.clicked.connect(Determine)

            # 添加一个取消按钮
            btn2 = QPushButton("取消", dialog)  # 创建一个按钮
            btn2.resize(75, 25)  # 设置按钮大小
            btn2.move(120, 110)
            btn2.clicked.connect(close_1)

            dialog.setWindowModality(Qt.NonModal)
            dialog.exec_()
            # ==========================================

        # ==========================================
        # 功能：读取用户选择转换命令为脚本并加载到文本框内
        # ==========================================
        command = self.comboBox.currentText()  # 返回选中的命令
        print(command)
        if command == "循环次数":
            loop_times()

        if command == "移动":
            move_cmd()

        if command == "下降":
            down_cmd()

        if command == "顶升":
            Lifting_cmd()

        if command == "旋转":
            Rotating_cmd()

        if command == "充电":
            Charging_cmd()

        if command == "退出充电":
            Exitcharge_cmd()
            
        if command == "设置托盘高度":
            pod_cmd()

        """
       # ==========================================
       # 功能：测试弹出对话框
       # ==========================================
        dialog = QDialog()
        btn = QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()
        """
        pass

    @pyqtSlot()
    def on_pushButton_Suspend_clicked(self):
        pass

    @pyqtSlot()
    def on_pushButton_Run_clicked(self):
        pass

    @pyqtSlot()
    def on_pushButton_Stop_clicked(self):
        pass
    
# ==========================================
# 功能：创建一个子线程，并接收原始数据，（已
# 丢弃不完整的数据帧
class Sum(QThread):
    ok_data = ''
    Error = ''
    Repeat_Data = ''
    # self.Raw_Data = []
    sinOut = pyqtSignal(str)
    global ser

    def __init__(self):
        super().__init__()
        self.m = 0

    def run(self):
        try:
            while (True):
                self.num = 0
                # n = ser.inWaiting()
                # print(n)
                self.data_D = binascii.b2a_hex(ser.read(1))  # 将ASCII码的字符串转换成十六进制
                # print(self.data_D)
                self.data = str(self.data_D.decode('utf-8'))  # 去掉字符串前面的符号"b"
                # print(self.data_D)
                # print(self.data)
                if self.data == "aa":  # 寻找帧头
                    # 找到帧头后将帧头和数据部分拼接在一起
                    while (True):
                        if self.data == "55" and self.num == 47:  # 判断是否是完整的一帧
                            self.ok_data = self.ok_data + "55"  # 将帧尾拼接到数据帧上
                            self.sinOut.emit(self.ok_data)  # 发射信号并将数据一并发送
                            self.ok_data = ''  # 清空上一帧数据
                            break

                        self.ok_data = self.ok_data + self.data  # 每一帧数据拼接
                        #print(self.ok_data)
                        self.num = self.num + 1  # 数据个数计数
                        # print(self.num)
                        if self.num > 48 or len(self.ok_data) > 100:
                            self.ok_data = ''
                            self.num = 0
                        self.data_D = binascii.b2a_hex(ser.read(1))  # 将ASCII码的字符串转换成十六进制
                        self.data = str(self.data_D.decode('utf-8'))  # 去掉字符串前面的符号"b"
                        # print(self.data)

                # self.sleep(0.5)

                time.sleep(0.05)
        except:
            ser.close()
            print("串口异常")
            # self.textEdit_AbnormalInformation.append("串口异常")

######################################
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())


