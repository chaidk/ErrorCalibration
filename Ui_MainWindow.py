# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ChaiPC\Documents\github\ErrorCalibration-main\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 551)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton\n"
"{\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QTextBrowser\n"
"{\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 958, 502))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.input_02 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_02.setFont(font)
        self.input_02.setText("")
        self.input_02.setObjectName("input_02")
        self.gridLayout_3.addWidget(self.input_02, 1, 2, 1, 1)
        self.input_44 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_44.setFont(font)
        self.input_44.setAutoFillBackground(False)
        self.input_44.setReadOnly(True)
        self.input_44.setObjectName("input_44")
        self.gridLayout_3.addWidget(self.input_44, 7, 4, 1, 1)
        self.input_64 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_64.setFont(font)
        self.input_64.setAutoFillBackground(False)
        self.input_64.setReadOnly(True)
        self.input_64.setObjectName("input_64")
        self.gridLayout_3.addWidget(self.input_64, 9, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 4, 1, 1)
        self.input_33 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_33.setFont(font)
        self.input_33.setObjectName("input_33")
        self.gridLayout_3.addWidget(self.input_33, 6, 3, 1, 1)
        self.input_13 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_13.setFont(font)
        self.input_13.setObjectName("input_13")
        self.gridLayout_3.addWidget(self.input_13, 4, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 9, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.input_63 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_63.setFont(font)
        self.input_63.setObjectName("input_63")
        self.gridLayout_3.addWidget(self.input_63, 9, 3, 1, 1)
        self.input_24 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_24.setFont(font)
        self.input_24.setAutoFillBackground(False)
        self.input_24.setReadOnly(True)
        self.input_24.setObjectName("input_24")
        self.gridLayout_3.addWidget(self.input_24, 5, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 12, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 1, 1, 1)
        self.input_53 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_53.setFont(font)
        self.input_53.setObjectName("input_53")
        self.gridLayout_3.addWidget(self.input_53, 8, 3, 1, 1)
        self.input_52 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_52.setFont(font)
        self.input_52.setObjectName("input_52")
        self.gridLayout_3.addWidget(self.input_52, 8, 2, 1, 1)
        self.input_43 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_43.setFont(font)
        self.input_43.setObjectName("input_43")
        self.gridLayout_3.addWidget(self.input_43, 7, 3, 1, 1)
        self.input_23 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_23.setFont(font)
        self.input_23.setObjectName("input_23")
        self.gridLayout_3.addWidget(self.input_23, 5, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 1)
        self.input_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_12.setFont(font)
        self.input_12.setObjectName("input_12")
        self.gridLayout_3.addWidget(self.input_12, 4, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 2, 1, 1)
        self.input_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_11.setFont(font)
        self.input_11.setText("")
        self.input_11.setObjectName("input_11")
        self.gridLayout_3.addWidget(self.input_11, 4, 1, 1, 1)
        self.input_32 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_32.setFont(font)
        self.input_32.setObjectName("input_32")
        self.gridLayout_3.addWidget(self.input_32, 6, 2, 1, 1)
        self.input_42 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_42.setFont(font)
        self.input_42.setObjectName("input_42")
        self.gridLayout_3.addWidget(self.input_42, 7, 2, 1, 1)
        self.input_34 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_34.setFont(font)
        self.input_34.setAutoFillBackground(False)
        self.input_34.setReadOnly(True)
        self.input_34.setObjectName("input_34")
        self.gridLayout_3.addWidget(self.input_34, 6, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)
        self.input_22 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_22.setFont(font)
        self.input_22.setObjectName("input_22")
        self.gridLayout_3.addWidget(self.input_22, 5, 2, 1, 1)
        self.input_54 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_54.setFont(font)
        self.input_54.setAutoFillBackground(False)
        self.input_54.setReadOnly(True)
        self.input_54.setObjectName("input_54")
        self.gridLayout_3.addWidget(self.input_54, 8, 4, 1, 1)
        self.input_14 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_14.setFont(font)
        self.input_14.setAutoFillBackground(False)
        self.input_14.setReadOnly(True)
        self.input_14.setObjectName("input_14")
        self.gridLayout_3.addWidget(self.input_14, 4, 4, 1, 1)
        self.input_62 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_62.setFont(font)
        self.input_62.setObjectName("input_62")
        self.gridLayout_3.addWidget(self.input_62, 9, 2, 1, 1)
        self.input_21 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_21.setFont(font)
        self.input_21.setText("")
        self.input_21.setObjectName("input_21")
        self.gridLayout_3.addWidget(self.input_21, 5, 1, 1, 1)
        self.input_51 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_51.setFont(font)
        self.input_51.setText("")
        self.input_51.setObjectName("input_51")
        self.gridLayout_3.addWidget(self.input_51, 8, 1, 1, 1)
        self.input_61 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_61.setFont(font)
        self.input_61.setText("")
        self.input_61.setObjectName("input_61")
        self.gridLayout_3.addWidget(self.input_61, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 5)
        self.input_82 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_82.setFont(font)
        self.input_82.setObjectName("input_82")
        self.gridLayout_3.addWidget(self.input_82, 11, 2, 1, 1)
        self.input_31 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_31.setFont(font)
        self.input_31.setText("")
        self.input_31.setObjectName("input_31")
        self.gridLayout_3.addWidget(self.input_31, 6, 1, 1, 1)
        self.input_41 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_41.setFont(font)
        self.input_41.setText("")
        self.input_41.setObjectName("input_41")
        self.gridLayout_3.addWidget(self.input_41, 7, 1, 1, 1)
        self.input_81 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_81.setFont(font)
        self.input_81.setText("")
        self.input_81.setObjectName("input_81")
        self.gridLayout_3.addWidget(self.input_81, 11, 1, 1, 1)
        self.input_73 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_73.setFont(font)
        self.input_73.setText("")
        self.input_73.setObjectName("input_73")
        self.gridLayout_3.addWidget(self.input_73, 10, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 11, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 2, 0, 1, 5)
        self.input_74 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_74.setFont(font)
        self.input_74.setAutoFillBackground(False)
        self.input_74.setReadOnly(True)
        self.input_74.setObjectName("input_74")
        self.gridLayout_3.addWidget(self.input_74, 10, 4, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.input_84 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_84.setFont(font)
        self.input_84.setAutoFillBackground(False)
        self.input_84.setReadOnly(True)
        self.input_84.setObjectName("input_84")
        self.gridLayout_3.addWidget(self.input_84, 11, 4, 1, 1)
        self.input_71 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_71.setFont(font)
        self.input_71.setText("")
        self.input_71.setObjectName("input_71")
        self.gridLayout_3.addWidget(self.input_71, 10, 1, 1, 1)
        self.input_72 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_72.setFont(font)
        self.input_72.setObjectName("input_72")
        self.gridLayout_3.addWidget(self.input_72, 10, 2, 1, 1)
        self.input_83 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_83.setFont(font)
        self.input_83.setText("")
        self.input_83.setObjectName("input_83")
        self.gridLayout_3.addWidget(self.input_83, 11, 3, 1, 1)
        self.btn_gen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.btn_gen.setFont(font)
        self.btn_gen.setObjectName("btn_gen")
        self.gridLayout_3.addWidget(self.btn_gen, 13, 0, 1, 5)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.input_01 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_01.setFont(font)
        self.input_01.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_01.setText("")
        self.input_01.setObjectName("input_01")
        self.gridLayout_3.addWidget(self.input_01, 1, 1, 1, 1)
        self.btn_reg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.btn_reg.setFont(font)
        self.btn_reg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_reg.setStyleSheet("")
        self.btn_reg.setObjectName("btn_reg")
        self.gridLayout_3.addWidget(self.btn_reg, 1, 4, 1, 1)
        self.input_03 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.input_03.setFont(font)
        self.input_03.setText("")
        self.input_03.setObjectName("input_03")
        self.gridLayout_3.addWidget(self.input_03, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_6)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_8)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.btn_reg.clicked.connect(MainWindow.start)
        self.action_4.triggered.connect(MainWindow.close)
        self.btn_gen.clicked.connect(MainWindow.generate)
        self.action_2.triggered.connect(MainWindow.configuration)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.input_01, self.input_02)
        MainWindow.setTabOrder(self.input_02, self.input_03)
        MainWindow.setTabOrder(self.input_03, self.btn_reg)
        MainWindow.setTabOrder(self.btn_reg, self.input_11)
        MainWindow.setTabOrder(self.input_11, self.input_12)
        MainWindow.setTabOrder(self.input_12, self.input_13)
        MainWindow.setTabOrder(self.input_13, self.input_21)
        MainWindow.setTabOrder(self.input_21, self.input_22)
        MainWindow.setTabOrder(self.input_22, self.input_23)
        MainWindow.setTabOrder(self.input_23, self.input_31)
        MainWindow.setTabOrder(self.input_31, self.input_32)
        MainWindow.setTabOrder(self.input_32, self.input_33)
        MainWindow.setTabOrder(self.input_33, self.input_41)
        MainWindow.setTabOrder(self.input_41, self.input_42)
        MainWindow.setTabOrder(self.input_42, self.input_43)
        MainWindow.setTabOrder(self.input_43, self.input_51)
        MainWindow.setTabOrder(self.input_51, self.input_52)
        MainWindow.setTabOrder(self.input_52, self.input_53)
        MainWindow.setTabOrder(self.input_53, self.input_61)
        MainWindow.setTabOrder(self.input_61, self.input_62)
        MainWindow.setTabOrder(self.input_62, self.input_63)
        MainWindow.setTabOrder(self.input_63, self.input_71)
        MainWindow.setTabOrder(self.input_71, self.input_72)
        MainWindow.setTabOrder(self.input_72, self.input_73)
        MainWindow.setTabOrder(self.input_73, self.input_81)
        MainWindow.setTabOrder(self.input_81, self.input_82)
        MainWindow.setTabOrder(self.input_82, self.input_83)
        MainWindow.setTabOrder(self.input_83, self.btn_gen)
        MainWindow.setTabOrder(self.btn_gen, self.input_14)
        MainWindow.setTabOrder(self.input_14, self.input_24)
        MainWindow.setTabOrder(self.input_24, self.input_34)
        MainWindow.setTabOrder(self.input_34, self.input_44)
        MainWindow.setTabOrder(self.input_44, self.input_54)
        MainWindow.setTabOrder(self.input_54, self.input_64)
        MainWindow.setTabOrder(self.input_64, self.input_74)
        MainWindow.setTabOrder(self.input_74, self.input_84)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "非线性误差校准工具"))
        self.input_02.setPlaceholderText(_translate("MainWindow", "启动风速(m/s)"))
        self.label_12.setText(_translate("MainWindow", "非线性误差绝对值(m/s)"))
        self.input_33.setPlaceholderText(_translate("MainWindow", "6"))
        self.input_13.setPlaceholderText(_translate("MainWindow", "2"))
        self.label_11.setText(_translate("MainWindow", "6"))
        self.label_4.setText(_translate("MainWindow", "实际风速值Vs（m/s)"))
        self.label_9.setText(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.input_63.setPlaceholderText(_translate("MainWindow", "12"))
        self.label_2.setText(_translate("MainWindow", "风表示值Vz（格） "))
        self.input_53.setPlaceholderText(_translate("MainWindow", "10"))
        self.input_52.setPlaceholderText(_translate("MainWindow", "60"))
        self.input_43.setPlaceholderText(_translate("MainWindow", "8"))
        self.input_23.setPlaceholderText(_translate("MainWindow", "4"))
        self.label_7.setText(_translate("MainWindow", "3"))
        self.label_8.setText(_translate("MainWindow", "4"))
        self.input_12.setPlaceholderText(_translate("MainWindow", "60"))
        self.label_10.setText(_translate("MainWindow", "每个点默认时间（秒）"))
        self.input_11.setPlaceholderText(_translate("MainWindow", "必填"))
        self.input_32.setPlaceholderText(_translate("MainWindow", "60"))
        self.input_42.setPlaceholderText(_translate("MainWindow", "60"))
        self.label_6.setText(_translate("MainWindow", "2"))
        self.input_22.setPlaceholderText(_translate("MainWindow", "60"))
        self.input_62.setPlaceholderText(_translate("MainWindow", "60"))
        self.input_21.setPlaceholderText(_translate("MainWindow", "必填"))
        self.input_51.setPlaceholderText(_translate("MainWindow", "必填"))
        self.input_61.setPlaceholderText(_translate("MainWindow", "选填"))
        self.label.setText(_translate("MainWindow", "非线性误差校准工具"))
        self.input_82.setPlaceholderText(_translate("MainWindow", "60"))
        self.input_31.setPlaceholderText(_translate("MainWindow", "必填"))
        self.input_41.setPlaceholderText(_translate("MainWindow", "必填"))
        self.input_81.setPlaceholderText(_translate("MainWindow", "选填"))
        self.input_73.setPlaceholderText(_translate("MainWindow", "14"))
        self.label_33.setText(_translate("MainWindow", "8"))
        self.label_32.setText(_translate("MainWindow", "7"))
        self.label_3.setText(_translate("MainWindow", "测量点"))
        self.input_71.setPlaceholderText(_translate("MainWindow", "选填"))
        self.input_72.setPlaceholderText(_translate("MainWindow", "60"))
        self.input_83.setPlaceholderText(_translate("MainWindow", "16"))
        self.btn_gen.setText(_translate("MainWindow", "生成报告"))
        self.label_14.setText(_translate("MainWindow", "精确度"))
        self.input_01.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.btn_reg.setText(_translate("MainWindow", "开始校准"))
        self.input_03.setPlaceholderText(_translate("MainWindow", "证书编号"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "使用指南"))
        self.action_3.setText(_translate("MainWindow", "关于"))
        self.action_2.setText(_translate("MainWindow", "设置"))
        self.action_4.setText(_translate("MainWindow", "退出"))
        self.action_6.setText(_translate("MainWindow", "使用指南"))
        self.action_8.setText(_translate("MainWindow", "关于"))

