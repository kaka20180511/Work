# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\温度传感器\Temp_X9\temp.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(888, 693)
        Dialog.setStyleSheet("    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    selection-background-color:#3daee9;\n"
"    selection-color: #eff0f1;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;")
        Dialog.setSizeGripEnabled(True)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(15, 24, 178, 79))
        self.label_5.setStyleSheet("background-color: rgb(90, 102, 117);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(12, 105, 181, 235))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(3, -3, 181, 230))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_port = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.comboBox_port.setFont(font)
        self.comboBox_port.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.comboBox_port.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.HongKong))
        self.comboBox_port.setObjectName("comboBox_port")
        self.verticalLayout.addWidget(self.comboBox_port)
        self.lineEdit_input_frequency = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.lineEdit_input_frequency.setFont(font)
        self.lineEdit_input_frequency.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.lineEdit_input_frequency.setObjectName("lineEdit_input_frequency")
        self.verticalLayout.addWidget(self.lineEdit_input_frequency)
        self.lineEdit_input_time = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.lineEdit_input_time.setFont(font)
        self.lineEdit_input_time.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.lineEdit_input_time.setObjectName("lineEdit_input_time")
        self.verticalLayout.addWidget(self.lineEdit_input_time)
        self.label_remain_time = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_remain_time.setFont(font)
        self.label_remain_time.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_remain_time.setObjectName("label_remain_time")
        self.verticalLayout.addWidget(self.label_remain_time)
        self.label_max_temperature = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_max_temperature.setFont(font)
        self.label_max_temperature.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_max_temperature.setObjectName("label_max_temperature")
        self.verticalLayout.addWidget(self.label_max_temperature)
        self.label_min_temperature = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_min_temperature.setFont(font)
        self.label_min_temperature.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_min_temperature.setObjectName("label_min_temperature")
        self.verticalLayout.addWidget(self.label_min_temperature)
        self.label_average_temperature = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_average_temperature.setFont(font)
        self.label_average_temperature.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_average_temperature.setObjectName("label_average_temperature")
        self.verticalLayout.addWidget(self.label_average_temperature)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(204, 9, 676, 736))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit_show_curve = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_show_curve.setGeometry(QtCore.QRect(0, 15, 676, 313))
        self.textEdit_show_curve.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.textEdit_show_curve.setObjectName("textEdit_show_curve")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(327, 0, 79, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_show = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_show.setGeometry(QtCore.QRect(0, 357, 676, 322))
        self.textEdit_show.setStyleSheet("    border: 1px solid #76797C;\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"    color: white;\n"
"    padding: 5px;\n"
"    opacity: 200;")
        self.textEdit_show.setObjectName("textEdit_show")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(327, 339, 79, 16))
        self.label_7.setObjectName("label_7")
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(15, 612, 175, 76))
        self.frame_5.setStyleSheet("\n"
"    background-color: rgb(90, 102, 117);;\n"
" ")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_start = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_start.setGeometry(QtCore.QRect(3, 6, 75, 31))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_stop.setGeometry(QtCore.QRect(3, 42, 168, 31))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_clear = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_clear.setGeometry(QtCore.QRect(96, 6, 75, 31))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(15, 366, 175, 241))
        self.frame_3.setStyleSheet("background-color: rgb(90, 102, 117);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textEdit_error = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_error.setGeometry(QtCore.QRect(6, 39, 163, 166))
        self.textEdit_error.setObjectName("textEdit_error")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(63, 15, 49, 16))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(81, 45, 28, 16))
        self.label_11.setStyleSheet("background-color: rgb(90, 102, 117);")
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        self.pushButton_clear.clicked.connect(self.textEdit_show.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "上海快仓温度测试软件"))
        self.lineEdit_input_frequency.setInputMask(_translate("Dialog", "999999"))
        self.lineEdit_input_frequency.setText(_translate("Dialog", "1"))
        self.lineEdit_input_time.setInputMask(_translate("Dialog", "999999"))
        self.lineEdit_input_time.setText(_translate("Dialog", "1"))
        self.label_remain_time.setText(_translate("Dialog", "0"))
        self.label_max_temperature.setText(_translate("Dialog", "0"))
        self.label_min_temperature.setText(_translate("Dialog", "0"))
        self.label_average_temperature.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "端口号"))
        self.label.setText(_translate("Dialog", "测量次数"))
        self.label_4.setText(_translate("Dialog", "测量间隔时间(秒)"))
        self.label_2.setText(_translate("Dialog", "剩余测量次数"))
        self.label_8.setText(_translate("Dialog", "最高温度"))
        self.label_9.setText(_translate("Dialog", "最低温度"))
        self.label_10.setText(_translate("Dialog", "平均温度"))
        self.label_6.setText(_translate("Dialog", "实时温度曲线"))
        self.label_7.setText(_translate("Dialog", "实时温度数据"))
        self.pushButton_start.setText(_translate("Dialog", "开始"))
        self.pushButton_stop.setText(_translate("Dialog", "停止"))
        self.pushButton_clear.setText(_translate("Dialog", "清除"))
        self.label_12.setText(_translate("Dialog", "错误记录"))
        self.label_11.setText(_translate("Dialog", "图标"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

