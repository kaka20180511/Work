# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Git_File\old_work\Work\socket_test\TCP_socket.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 575)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit_IP_add = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_IP_add.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_IP_add.setObjectName("lineEdit_IP_add")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label.setObjectName("label")
        self.textEdit_Receive = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Receive.setGeometry(QtCore.QRect(180, 60, 421, 401))
        self.textEdit_Receive.setObjectName("textEdit_Receive")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(180, 40, 81, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_Connect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Connect.setGeometry(QtCore.QRect(20, 100, 111, 51))
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.pushButton_interrupt = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_interrupt.setGeometry(QtCore.QRect(20, 230, 111, 51))
        self.pushButton_interrupt.setObjectName("pushButton_interrupt")
        self.textEdit_Send = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_Send.setGeometry(QtCore.QRect(180, 490, 351, 71))
        self.textEdit_Send.setObjectName("textEdit_Send")
        self.pushButton_Send = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Send.setGeometry(QtCore.QRect(540, 490, 61, 71))
        self.pushButton_Send.setObjectName("pushButton_Send")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(180, 470, 81, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 360, 111, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 510, 111, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(self.textEdit_Receive.clear)
        self.pushButton_5.clicked.connect(self.textEdit_Send.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "机器IP地址"))
        self.label_2.setText(_translate("MainWindow", "接收数据"))
        self.pushButton_Connect.setText(_translate("MainWindow", "连接"))
        self.pushButton_interrupt.setText(_translate("MainWindow", "断开"))
        self.pushButton_Send.setText(_translate("MainWindow", "发送"))
        self.label_3.setText(_translate("MainWindow", "发送数据"))
        self.pushButton_4.setText(_translate("MainWindow", "清空接收"))
        self.pushButton_5.setText(_translate("MainWindow", "清空发送"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

