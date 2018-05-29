# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\TestPyQt5\fault_diagnosis\Move_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    
    def setupUi_2(self, Dialog):
        accept1 = 0
        Dialog.setObjectName("Dialog")
        Dialog.resize(219, 144)
        Dialog.setStyleSheet("    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    selection-background-color:#3daee9;\n"
"    selection-color: #eff0f1;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;")
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 24, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 64, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_move_X = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_move_X.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit_move_X.setObjectName("lineEdit_move_X")
        self.lineEdit_move_Y = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_move_Y.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.lineEdit_move_Y.setObjectName("lineEdit_move_Y")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(30, 100, 75, 23))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Dialog)
        self.pushButton_cancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "X坐标："))
        self.label_2.setText(_translate("Dialog", "Y坐标："))
        self.pushButton_ok.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi_2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

