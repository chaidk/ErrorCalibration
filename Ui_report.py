# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ChaiPC\Documents\github\ErrorCalibration-main\report.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class Ui_reportwin(object):
    def setupUi(self, reportwin):
        reportwin.setObjectName("reportwin")
        reportwin.resize(650, 860)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(reportwin.sizePolicy().hasHeightForWidth())
        reportwin.setSizePolicy(sizePolicy)
        reportwin.setMinimumSize(QtCore.QSize(650, 860))
        reportwin.setMaximumSize(QtCore.QSize(650, 860))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        reportwin.setWindowIcon(icon)
        reportwin.setAutoFillBackground(True)
        reportwin.setStyleSheet("")
        self.browser = QtWebEngineWidgets.QWebEngineView(reportwin)
        self.browser.setEnabled(True)
        self.browser.setGeometry(QtCore.QRect(0, 0, 650, 830))
        self.browser.setMinimumSize(QtCore.QSize(650, 830))
        self.browser.setMaximumSize(QtCore.QSize(650, 830))
        self.browser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.browser.setUrl(QtCore.QUrl("about:blank"))
        self.browser.setObjectName("browser")
        self.pushButton = QtWidgets.QPushButton(reportwin)
        self.pushButton.setGeometry(QtCore.QRect(0, 830, 650, 30))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(reportwin)
        self.pushButton.clicked.connect(reportwin.screen_shot)
        QtCore.QMetaObject.connectSlotsByName(reportwin)

    def retranslateUi(self, reportwin):
        _translate = QtCore.QCoreApplication.translate
        reportwin.setWindowTitle(_translate("reportwin", "Dialog"))
        self.pushButton.setText(_translate("reportwin", "保存报告"))

from PyQt5 import QtWebEngineWidgets
