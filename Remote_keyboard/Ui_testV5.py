# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Git_File\old_work\Remote_keyboard\testV5.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(70, 140, 311, 311))
        self.listView.setStyleSheet("QGroupBox {\n"
"  border: 1.5px solid rgb(36, 36, 36);\n"
"}\n"
"border:0; ")
        self.listView.setObjectName("listView")
        self.pushButton_up = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_up.setGeometry(QtCore.QRect(180, 170, 91, 61))
        self.pushButton_up.setStyleSheet("")
        self.pushButton_up.setObjectName("pushButton_up")
        self.pushButton_right = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_right.setGeometry(QtCore.QRect(280, 260, 91, 61))
        self.pushButton_right.setStyleSheet("")
        self.pushButton_right.setObjectName("pushButton_right")
        self.pushButton_left = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_left.setGeometry(QtCore.QRect(80, 260, 91, 61))
        self.pushButton_left.setStyleSheet("")
        self.pushButton_left.setObjectName("pushButton_left")
        self.pushButton_down = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_down.setGeometry(QtCore.QRect(180, 350, 91, 61))
        self.pushButton_down.setStyleSheet("")
        self.pushButton_down.setObjectName("pushButton_down")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(70, 90, 113, 20))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.pushButton_connect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(210, 90, 75, 23))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.listView_2 = QtWidgets.QListView(self.centralWidget)
        self.listView_2.setGeometry(QtCore.QRect(400, 140, 311, 311))
        self.listView_2.setObjectName("listView_2")
        self.pushButton_pod_up = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_pod_up.setGeometry(QtCore.QRect(430, 150, 91, 61))
        self.pushButton_pod_up.setStyleSheet("")
        self.pushButton_pod_up.setObjectName("pushButton_pod_up")
        self.pushButton_pod_pown = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_pod_pown.setGeometry(QtCore.QRect(430, 350, 91, 61))
        self.pushButton_pod_pown.setStyleSheet("")
        self.pushButton_pod_pown.setObjectName("pushButton_pod_pown")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(550, 260, 121, 61))
        self.pushButton_stop.setStyleSheet("")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(400, 90, 54, 12))
        self.label.setObjectName("label")
        self.spinBox_adjust_speed = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_adjust_speed.setGeometry(QtCore.QRect(460, 90, 71, 22))
        self.spinBox_adjust_speed.setMinimum(1)
        self.spinBox_adjust_speed.setMaximum(4)
        self.spinBox_adjust_speed.setObjectName("spinBox_adjust_speed")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_up.setText(_translate("MainWindow", "上（shift+W）"))
        self.pushButton_right.setText(_translate("MainWindow", "上（shift+D）"))
        self.pushButton_left.setText(_translate("MainWindow", "左（shift+A）"))
        self.pushButton_down.setText(_translate("MainWindow", "上（shift+S）"))
        self.pushButton_connect.setText(_translate("MainWindow", "连接"))
        self.pushButton_pod_up.setText(_translate("MainWindow", "顶升（shift+Q）"))
        self.pushButton_pod_pown.setText(_translate("MainWindow", "下降（shift+Z）"))
        self.pushButton_stop.setText(_translate("MainWindow", "急停（shift+空格）"))
        self.label.setText(_translate("MainWindow", "速度等级"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

