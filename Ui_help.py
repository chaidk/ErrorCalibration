# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ChaiPC\Documents\github\ErrorCalibration-main\help.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class Ui_helpwin(object):
    def setupUi(self, helpwin):
        helpwin.setObjectName("helpwin")
        helpwin.resize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(helpwin.sizePolicy().hasHeightForWidth())
        helpwin.setSizePolicy(sizePolicy)
        helpwin.setMinimumSize(QtCore.QSize(500, 200))
        helpwin.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        helpwin.setFont(font)
        helpwin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        helpwin.setWindowIcon(icon)
        helpwin.setAutoFillBackground(False)
        helpwin.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.content = QtWidgets.QTextEdit(helpwin)
        self.content.setGeometry(QtCore.QRect(50, 0, 551, 211))
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setUndoRedoEnabled(False)
        self.content.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.content.setAcceptRichText(True)
        self.content.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.content.setObjectName("content")

        self.retranslateUi(helpwin)
        QtCore.QMetaObject.connectSlotsByName(helpwin)

    def retranslateUi(self, helpwin):
        _translate = QtCore.QCoreApplication.translate
        helpwin.setWindowTitle(_translate("helpwin", "帮助"))
        self.content.setHtml(_translate("helpwin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">使用说明：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">1.输入精确度（选填，默认为0.00）。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">  例：如需保留4位小数，输入0.0000。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2.输入启动风速，单位为&quot;m/s&quot;。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">3.输入证书编号（选填，空缺则自动生成编号）。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">4.分别输入不少于5组测量点数据。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">5.点击开始校准计算非线性误差绝对值，单位为&quot;m/s&quot;。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">6.点击生成报告即可保存报告，存储路径为&quot;report&quot;文件夹。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))

