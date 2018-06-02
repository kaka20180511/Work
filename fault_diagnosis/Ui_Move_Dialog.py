# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\Work\fault_diagnosis\Move_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi_2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(223, 153)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 100, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        #self.buttonBox.accepted.connect(Dialog.er)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def dataTime(self):
        return self.lineEdit_move_Y.text()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "X坐标："))
        self.label_2.setText(_translate("Dialog", "Y坐标："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi_2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

