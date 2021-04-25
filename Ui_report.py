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
        reportwin.resize(501, 703)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(reportwin)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 500, 700))
        self.webEngineView.setMinimumSize(QtCore.QSize(500, 700))
        self.webEngineView.setMaximumSize(QtCore.QSize(500, 700))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(reportwin)
        QtCore.QMetaObject.connectSlotsByName(reportwin)

    def retranslateUi(self, reportwin):
        _translate = QtCore.QCoreApplication.translate
        reportwin.setWindowTitle(_translate("reportwin", "Dialog"))

from PyQt5 import QtWebEngineWidgets
