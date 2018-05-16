import threading  # 加载线程模块
import serial  # 加载串口模块
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Read_Port import *
from agreement_cmd import *
from Data_reduction import *
from data_save import *
from file_rename import *
from Ui_temp import Ui_Dialog

stop_flag = 0 # 停止程序标志位(1是终止)
class reconsitution_temp(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(reconsitution_temp, self).__init__(parent)
        self.setupUi(self)
        # ==============================================
        # 用for循环将所有端口号展示出来
        ports = Read_Port() #调用获取端口号函数
        #print(Read_Port())
        for port in ports:
            self.comboBox_port.addItem(port) 
        # ==============================================   
    
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        global stop_flag
        stop_flag = 0
        # ==============================================
        # 当按键被按下后，按键变成不可选
        self.pushButton_start.setEnabled(False)
        #self.pushButton_start.setEnabled(True)
        # ==============================================
        
        # ==============================================
        # 或取UI界面的用户选项和输入值
        self.input_time = self.lineEdit_input_time.text()  # 获取用户输入的时间间隔
        self.input_time = int(self.input_time)  # 字符转整形
        self.input_frequency = self.lineEdit_input_frequency.text()  # 获取用户输入的测量次数
        self.input_frequency = int(self.input_frequency)  # 字符转整形
        # ==============================================
        print(self.input_time)
        print(self.input_frequency)
        
        # ==============================================
        # 这是新的配置和调用串口的方法
        self.ser = serial.Serial()              #串口模块
        port_com = self.comboBox_port.currentText() #返回选中的串口号
        self.ser.port = port_com
        print(port_com)
        self.ser.baudrate = 9600 #设置串口波特率
        self.ser.bytesize = serial.EIGHTBITS 
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.parity = serial.PARITY_NONE
        self.ser.timeout=0.1
        # ==============================================
        self.ser.open()  #打开串口
        
        # ==============================================
        #主函数，重复查询和读取串口从这里开始
        def TXD():
            #global stop_flag
            while(self.input_frequency):
                if stop_flag == 1: 
                    break
                self.ser.writelines(agreement_cmd())  # 向串口中写入数据
                #time.sleep(0.01)
                #read_data = self.ser.readall() # 读取所有数据会导致串口超时
                read_data = self.ser.readline()
                #print(read_data)
                full_data = data_reduction(read_data)
                #print(full_data)
                #self.textEdit_show.setPlainText(full_data)  
                self.textEdit_show.append(full_data)  # 在多行文本框中显示读取的数据
                data_save(full_data)
                time.sleep(self.input_time)
                self.input_frequency = self.input_frequency -1
                
                # ========================================
                # 调用子程序将温度数据文件重命名
                if self.input_frequency == 0:
                    file_rename() # # 重名名文件
                # ========================================
                
                # ========================================
                # 如果程序执行完开始按钮变成可以选中
                if self.input_frequency == 0:
                    self.pushButton_start.setEnabled(True)
                # ========================================
                
                self.label_remain_time.setText(str(self.input_frequency))  # 在标签中显示剩余测量次数
                
        # ==============================================
        
        # ==============================================
        # 创建线程并启动线程
        ReadThread = threading.Thread(target=TXD) #线程调用读取串口数据函数
        ReadThread .start() #启动线程
        # ==============================================
        
        pass
 
    
    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        global stop_flag
        stop_flag = 1
        self.ser.close()  #关闭串口
        # ============================
        # 如果文件不存在就让程序跳过，防止误操作
        try:
            file_rename() # 重名名文件
        except:
            pass
        # ============================
        #self.pushButton_stop.setEnabled(False)
        self.pushButton_start.setEnabled(True)
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = reconsitution_temp()
    dlg.show()
    sys.exit(app.exec_())
