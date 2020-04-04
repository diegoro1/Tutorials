# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorial_qt.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(310, 460, 141, 51))
        self.button_1.setObjectName("button_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(290, 170, 201, 71))
        self.label_1.setTextFormat(QtCore.Qt.PlainText)
        self.label_1.setObjectName("label_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuDont_Type_hEre = QtWidgets.QMenu(self.menubar)
        self.menuDont_Type_hEre.setObjectName("menuDont_Type_hEre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionYay = QtWidgets.QAction(MainWindow)
        self.actionYay.setObjectName("actionYay")
        self.actionNo_Way = QtWidgets.QAction(MainWindow)
        self.actionNo_Way.setObjectName("actionNo_Way")
        self.actionHow_fun = QtWidgets.QAction(MainWindow)
        self.actionHow_fun.setObjectName("actionHow_fun")
        self.actionWhy = QtWidgets.QAction(MainWindow)
        self.actionWhy.setObjectName("actionWhy")
        self.menuFIle.addAction(self.actionYay)
        self.menuFIle.addAction(self.actionNo_Way)
        self.menuFIle.addAction(self.actionHow_fun)
        self.menuDont_Type_hEre.addAction(self.actionWhy)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuDont_Type_hEre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_1.setText(_translate("MainWindow", "What are you?"))
        self.label_1.setText(_translate("MainWindow", "You are amazing!"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuDont_Type_hEre.setTitle(_translate("MainWindow", "Dont Type hEre"))
        self.actionYay.setText(_translate("MainWindow", "Yay"))
        self.actionNo_Way.setText(_translate("MainWindow", "No Way!"))
        self.actionHow_fun.setText(_translate("MainWindow", "How fun!"))
        self.actionWhy.setText(_translate("MainWindow", "Why!"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
