# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ChaiPC\Documents\github\ErrorCalibration-main\config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class Ui_configwin(object):
    def setupUi(self, configwin):
        configwin.setObjectName("configwin")
        configwin.resize(540, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(configwin.sizePolicy().hasHeightForWidth())
        configwin.setSizePolicy(sizePolicy)
        configwin.setMinimumSize(QtCore.QSize(540, 160))
        configwin.setMaximumSize(QtCore.QSize(540, 160))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        configwin.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(configwin)
        self.buttonBox.setGeometry(QtCore.QRect(450, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(configwin)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 361, 150))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.company = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.company.setFont(font)
        self.company.setText("")
        self.company.setPlaceholderText("")
        self.company.setObjectName("company")
        self.gridLayout.addWidget(self.company, 0, 1, 1, 1)
        self.pwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pwd.setFont(font)
        self.pwd.setText("")
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setPlaceholderText("")
        self.pwd.setObjectName("pwd")
        self.gridLayout.addWidget(self.pwd, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.code = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.code.setFont(font)
        self.code.setText("")
        self.code.setPlaceholderText("")
        self.code.setObjectName("code")
        self.gridLayout.addWidget(self.code, 1, 1, 1, 1)

        self.retranslateUi(configwin)
        self.buttonBox.accepted.connect(configwin.setConfig)
        self.buttonBox.rejected.connect(configwin.close)
        QtCore.QMetaObject.connectSlotsByName(configwin)
        configwin.setTabOrder(self.company, self.code)
        configwin.setTabOrder(self.code, self.pwd)

    def retranslateUi(self, configwin):
        _translate = QtCore.QCoreApplication.translate
        configwin.setWindowTitle(_translate("configwin", "设置"))
        self.label_16.setText(_translate("configwin", "修改密码"))
        self.label_14.setText(_translate("configwin", "公司名称"))
        self.label_15.setText(_translate("configwin", "证书编号"))

