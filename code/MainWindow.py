# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 20, 471, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblKeyword = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblKeyword.setObjectName("lblKeyword")
        self.horizontalLayout.addWidget(self.lblKeyword)
        self.tbxKeyword = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.tbxKeyword.setObjectName("tbxKeyword")
        self.horizontalLayout.addWidget(self.tbxKeyword)
        self.btnSearch = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(140, 290, 471, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnImg_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btnImg_1.setObjectName("btnImg_1")
        self.horizontalLayout_3.addWidget(self.btnImg_1)
        self.btnImg_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btnImg_2.setObjectName("btnImg_2")
        self.horizontalLayout_3.addWidget(self.btnImg_2)
        self.btnImg_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btnImg_3.setObjectName("btnImg_3")
        self.horizontalLayout_3.addWidget(self.btnImg_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 120, 471, 166))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.img_1.setObjectName("img_1")
        self.horizontalLayout_2.addWidget(self.img_1)
        self.img_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.img_2.setObjectName("img_2")
        self.horizontalLayout_2.addWidget(self.img_2)
        self.img_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.img_3.setObjectName("img_3")
        self.horizontalLayout_2.addWidget(self.img_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(140, 330, 471, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnDownload_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btnDownload_1.setObjectName("btnDownload_1")
        self.horizontalLayout_4.addWidget(self.btnDownload_1)
        self.btnDownload_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btnDownload_2.setObjectName("btnDownload_2")
        self.horizontalLayout_4.addWidget(self.btnDownload_2)
        self.btnDownload_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btnDownload_3.setObjectName("btnDownload_3")
        self.horizontalLayout_4.addWidget(self.btnDownload_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblKeyword.setText(_translate("MainWindow", "Keyword : "))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.btnImg_1.setText(_translate("MainWindow", "Git"))
        self.btnImg_2.setText(_translate("MainWindow", "Git"))
        self.btnImg_3.setText(_translate("MainWindow", "Git"))
        self.img_1.setText(_translate("MainWindow", "foto 1"))
        self.img_2.setText(_translate("MainWindow", "foto 2"))
        self.img_3.setText(_translate("MainWindow", "foto 3"))
        self.btnDownload_1.setText(_translate("MainWindow", "İndir"))
        self.btnDownload_2.setText(_translate("MainWindow", "İndir"))
        self.btnDownload_3.setText(_translate("MainWindow", "İndir"))
