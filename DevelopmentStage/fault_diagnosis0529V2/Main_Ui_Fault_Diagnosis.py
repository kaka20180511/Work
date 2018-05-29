# ==========================================
# 功能：小车诊断工具
# 2018-05-28 longshenglin
# ==========================================
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from Ui_Move_Dialog import *
# from Ui_Move_Dialog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QInputDialog

from Ui_Main_Ui_Fault_Diagnosis import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow, Ui_Dialog):
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


######################################
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())


