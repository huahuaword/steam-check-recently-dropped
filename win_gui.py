# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import Qt

class Ui_login_MainWindow(object):
    def setupUi(self, login_MainWindow):
        login_MainWindow.setObjectName("login_MainWindow")
        login_MainWindow.setEnabled(True)
        login_MainWindow.resize(575, 392)
        login_MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(login_MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 391, 79))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # 启用自动换行
        self.label_3.setWordWrap(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 150, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 200, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 150, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 280, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        login_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 22))
        self.menubar.setObjectName("menubar")
        login_MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(login_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(login_MainWindow)

    def retranslateUi(self, login_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        login_MainWindow.setWindowTitle(_translate("login_MainWindow", "MainWindow"))
        self.label_3.setText(_translate("login_MainWindow", "免费试用中\n纯本地运行 不中转任何私人服务器\nQ群：952966566 获取最新密码"))
        self.label_2.setText(_translate("login_MainWindow", "密码："))
        self.label.setText(_translate("login_MainWindow", "用户名："))
        self.lineEdit_2.setText(_translate("login_MainWindow", ""))
        self.pushButton.setText(_translate("login_MainWindow", "登录"))

class Ui_task_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.accTable = QtWidgets.QTableWidget(self.centralwidget)
        self.accTable.setGeometry(QtCore.QRect(0, 0, 711, 401))
        self.accTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.accTable.setObjectName("accTable")
        self.accTable.setColumnCount(10)

        self.accTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(9, item)
        self.accTable.horizontalHeader().setCascadingSectionResizes(False)
        self.accTable.horizontalHeader().setDefaultSectionSize(85)
        self.accTable.horizontalHeader().setSortIndicatorShown(False)
        self.accTable.horizontalHeader().setStretchLastSection(False)
        # 为每一列设置特定的列宽
        self.accTable.setColumnWidth(0, 30)  # 为第一列设置100像素宽
        self.accTable.setColumnWidth(1, 85)  # 为第二列设置150像素宽
        self.accTable.setColumnWidth(2, 20)  # 为第三列设置150像素宽
        self.accTable.setColumnWidth(3, 20)  # 以此类推...
        self.accTable.setColumnWidth(4, 20)
        self.accTable.setColumnWidth(5, 85)
        self.accTable.setColumnWidth(6, 100)
        self.accTable.setColumnWidth(7, 70)
        self.accTable.setColumnWidth(8, 200)
        self.accTable.setColumnWidth(9, 70)
        self.fuctionGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.fuctionGroup.setGeometry(QtCore.QRect(720, 0, 201, 401))
        self.fuctionGroup.setObjectName("fuctionGroup")
        self.addAccBut = QtWidgets.QPushButton(self.fuctionGroup)
        self.addAccBut.setGeometry(QtCore.QRect(10, 270, 91, 31))
        self.addAccBut.setObjectName("addAccBut")
        self.startTaskBut = QtWidgets.QPushButton(self.fuctionGroup)
        self.startTaskBut.setGeometry(QtCore.QRect(50, 330, 91, 31))
        self.startTaskBut.setObjectName("startTaskBut")
        self.pop3Edit = QtWidgets.QLineEdit(self.fuctionGroup)
        self.pop3Edit.setGeometry(QtCore.QRect(80, 29, 111, 31))
        self.pop3Edit.setObjectName("pop3Edit")
        self.pop3Label = QtWidgets.QLabel(self.fuctionGroup)
        self.pop3Label.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.pop3Label.setObjectName("pop3Label")
        self.threadNumEdit = QtWidgets.QLineEdit(self.fuctionGroup)
        self.threadNumEdit.setGeometry(QtCore.QRect(80, 79, 111, 31))
        self.threadNumEdit.setObjectName("pop3Edit")
        self.threadNumLabel = QtWidgets.QLabel(self.fuctionGroup)
        self.threadNumLabel.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.threadNumLabel.setObjectName("pop3Label")
        self.outputAccBut = QtWidgets.QPushButton(self.fuctionGroup)
        self.outputAccBut.setGeometry(QtCore.QRect(110, 270, 91, 31))
        self.outputAccBut.setObjectName("outputAccBut")
        # self.checkBox = QtWidgets.QCheckBox(self.fuctionGroup)
        # self.checkBox.setEnabled(True)
        # self.checkBox.setGeometry(QtCore.QRect(20, 80, 81, 31))
        # self.checkBox.setObjectName("checkBox")
        self.msgGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.msgGroup.setGeometry(QtCore.QRect(10, 410, 701, 171))
        self.msgGroup.setObjectName("msgGroup")
        self.msgEdit = QtWidgets.QTextEdit(self.msgGroup)
        self.msgEdit.setEnabled(True)
        self.msgEdit.setGeometry(QtCore.QRect(10, 20, 681, 141))
        self.msgEdit.setObjectName("msgEdit")
        self.fuctionGroup.raise_()
        self.msgGroup.raise_()
        self.accTable.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.addAccBut.clicked.connect(self.load_accounts_from_file)
        self.startTaskBut.clicked.connect(self.toggle_task)
        # 开启表格的右键菜单功能
        self.accTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.accTable.customContextMenuRequested.connect(self.openMenu)
        self.threadNumEdit.setText(str(1))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.accTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "账户"))
        item = self.accTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "密码"))
        item = self.accTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "邮箱"))
        item = self.accTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "邮箱密码"))
        item = self.accTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "登陆状态"))
        item = self.accTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "最近掉落"))
        item = self.accTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "掉落数量"))
        item = self.accTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "掉落日期"))
        item = self.accTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "掉落价格"))
        self.fuctionGroup.setTitle(_translate("MainWindow", "功能区"))
        self.addAccBut.setText(_translate("MainWindow", "导入账号"))
        self.startTaskBut.setText(_translate("MainWindow", "开始"))
        self.pop3Label.setText(_translate("MainWindow", "POP3地址"))
        self.threadNumLabel.setText(_translate("MainWindow", "线程数"))
        self.outputAccBut.setText(_translate("MainWindow", "导出账号"))
        # self.checkBox.setText(_translate("MainWindow", "读取Mf文件"))
        self.msgGroup.setTitle(_translate("MainWindow", "日志"))