# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ChaiPC\Documents\github\ErrorCalibration-main\report.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reportwin(object):
    def setupUi(self, reportwin):
        reportwin.setObjectName("reportwin")
        reportwin.resize(752, 1052)
        self.browser = QtWebEngineWidgets.QWebEngineView(reportwin)
        self.browser.setGeometry(QtCore.QRect(0, 0, 750, 1100))
        self.browser.setMinimumSize(QtCore.QSize(750, 1100))
        self.browser.setMaximumSize(QtCore.QSize(1000, 1100))
        self.browser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.browser.setUrl(QtCore.QUrl("about:blank"))
        self.browser.setObjectName("browser")

        self.retranslateUi(reportwin)
        QtCore.QMetaObject.connectSlotsByName(reportwin)

    def retranslateUi(self, reportwin):
        _translate = QtCore.QCoreApplication.translate
        reportwin.setWindowTitle(_translate("reportwin", "Dialog"))

from PyQt5 import QtWebEngineWidgets