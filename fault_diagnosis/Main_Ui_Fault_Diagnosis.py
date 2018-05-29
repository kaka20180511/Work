# ==========================================
# 功能：小车诊断工具
# 2018-05-28 longshenglin
# ==========================================
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from Ui_Move_Dialog import *
#from Ui_Move_Dialog import *
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
        #self.setupUi_2(self)
        
    # ==========================================
    # 功能：读取用户选择转换命令为脚本并加载到文本框内
    # ==========================================
    @pyqtSlot()
    def on_pushButton_Add_Cmd_clicked(self):
        
        
        def move():
            self.Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi_2(self.Dialog)
            self.Dialog.show()
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


