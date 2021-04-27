# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ChaiPC\Documents\github\ErrorCalibration-main\alert.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class Ui_alertwin(object):
    def setupUi(self, alertwin):
        alertwin.setObjectName("alertwin")
        alertwin.resize(400, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(alertwin.sizePolicy().hasHeightForWidth())
        alertwin.setSizePolicy(sizePolicy)
        alertwin.setMinimumSize(QtCore.QSize(400, 100))
        alertwin.setMaximumSize(QtCore.QSize(400, 100))
        alertwin.setSizeIncrement(QtCore.QSize(400, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        alertwin.setWindowIcon(icon)
        alertwin.setAutoFillBackground(False)
        alertwin.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.buttonBox = QtWidgets.QDialogButtonBox(alertwin)
        self.buttonBox.setGeometry(QtCore.QRect(50, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.content = QtWidgets.QLabel(alertwin)
        self.content.setGeometry(QtCore.QRect(60, 0, 281, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setMinimumSize(QtCore.QSize(1, 0))
        self.content.setObjectName("content")

        self.retranslateUi(alertwin)
        self.buttonBox.accepted.connect(alertwin.close)
        self.buttonBox.rejected.connect(alertwin.close)
        QtCore.QMetaObject.connectSlotsByName(alertwin)

    def retranslateUi(self, alertwin):
        _translate = QtCore.QCoreApplication.translate
        alertwin.setWindowTitle(_translate("alertwin", "提示"))
        self.content.setText(_translate("alertwin", "TextLabel"))

