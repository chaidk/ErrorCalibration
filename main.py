from PyQt5.QtWidgets import  QApplication,QMainWindow,QWidget,QPushButton,QDialog
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from Ui_MainWindow import Ui_MainWindow, QtCore
from Ui_config import Ui_configwin, QtCore
from Ui_report import Ui_reportwin, QtCore
from Ui_alert import Ui_alertwin, QtCore
from Ui_help import Ui_helpwin, QtCore

#import pandas as pd
from pandas import DataFrame
#import sys
from sys import argv,exit
#import os
from os import remove,rename,listdir,system
#import json
from json import load,dump
#import datetime
from datetime import datetime
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from decimal import Decimal

import encrypt

def load_conf():
    with open('app/config.json', 'r', encoding='utf8') as fp:
        conf = load(fp)
        return conf


def set_conf(company, code, pwd, key):
    conf = load_conf()
    company_h = encrypt.encrypt(company, key, 1)
    conf['para'] = company_h
    conf['code'] = code
    if pwd == 'pwd16968':
        with open('app/config.json', 'w', encoding='utf8') as fp:
            conf = dump(conf, fp, ensure_ascii=False)
            alertWindow.__init__('修改完成！', '修改完成')
            alertWindow.show()
            print('修改完成')
    else:
        alertWindow.__init__('密码错误！', '修改完成')
        alertWindow.show()
        print('密码错误')


def to_decimal(num, exp="0.00") -> Decimal:
    if not num:
        return Decimal("0").quantize(exp=Decimal(exp))
    if not isinstance(num, str):
        num = str(num)
    return Decimal(num).quantize(exp=Decimal(exp))


def reg(features, t, target, dcm):
    err = []
    t_value = (features[-1]-features[0])/(len(features)-1)
    model = LinearRegression()
    df_features = DataFrame(features).values.reshape(-1, 1)
    df_target = DataFrame(target)
    model.fit(df_features, df_target)
    intercept = float(model.intercept_)
    coef = float(model.coef_[0])
    for i in range(len(features)):
        x = features[0] + i * t_value
        y = coef * x + intercept
        e = abs((y - target[i]))
        e = str(to_decimal(e, dcm))
        print(i, x, y, t_value, e)
        err.append(e)
    return to_decimal(intercept, dcm), to_decimal(coef, dcm), err


def savefig(coef, intercept, x_data, y_data):
    print(x_data, coef, intercept)
    print(y_data)
    y_data = [intercept * x + coef for x in x_data]
    plt.clf()
    plt.figure('Grid', figsize=(5, 3.5), dpi=100)
    plt.title("校准曲线", fontsize=20, fontproperties="SimHei")
    plt.xlabel("风表示值Vz（格/s） ", fontsize=14, fontproperties="SimHei")
    plt.ylabel("实际风速值Vs（m/s)", fontsize=14, fontproperties="SimHei")
    plt.yticks(y_data)
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.5))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.3))

    # 紧凑布局
    plt.tight_layout()
    ax.grid(which='major', axis="both", linewidth=0.25,
            linestyle='-', color='gray')
    ax.grid(which='minor', axis="both", linewidth=0.25,
            linestyle='-', color='gray')
    plt.plot(x_data, y_data)
    plt.legend()
    try:
        remove('app/temdata001')
    except:
        pass
    plt.savefig('app/temdata001.png')
    rename('app/temdata001.png', 'app/temdata001')


def fnum(code):
    num = 1
    td = datetime.today().strftime('%Y%m%d')
    flist = listdir('report')
    start = len(code)
    for fname in flist:
        fname = fname[start:start+8]
        if fname.find(td) is not -1:
            num += 1
    fnum = code + td + '%02d' % num
    return fnum


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.para = [
            [self.input_01,
             self.input_02,
             self.input_03],
            [self.input_11,
             self.input_12,
             self.input_13,
             self.input_14],
            [self.input_21,
             self.input_22,
             self.input_23,
             self.input_24],
            [self.input_31,
             self.input_32,
             self.input_33,
             self.input_34],
            [self.input_41,
             self.input_42,
             self.input_43,
             self.input_44],
            [self.input_51,
             self.input_52,
             self.input_53,
             self.input_54],
            [self.input_61,
             self.input_62,
             self.input_63,
             self.input_64],
            [self.input_71,
             self.input_72,
             self.input_73,
             self.input_74],
            [self.input_81,
             self.input_82,
             self.input_83,
             self.input_84]
        ]

        dcm_reg = QtCore.QRegExp(r"0\.[0]{4}")
        int_reg = QtCore.QRegExp(r"[0-9]{4}")
        float_reg = QtCore.QRegExp(r"[0-9]{1,4}\.[0-9]{4}")
        input_reg = QtCore.QRegExp(r"[a-zA-Z0-9]{16}")
        dcm_validator = QtGui.QRegExpValidator(dcm_reg)
        int_validator = QtGui.QRegExpValidator(int_reg)
        float_validator = QtGui.QRegExpValidator(float_reg)
        input_validator = QtGui.QRegExpValidator(input_reg)
        self.para[0][0].setValidator(dcm_validator)
        self.para[0][1].setValidator(float_validator)
        self.para[0][2].setValidator(input_validator)
        for i in range(1, 9):
            self.para[i][0].setValidator(float_validator)
            self.para[i][1].setValidator(int_validator)
            self.para[i][2].setValidator(int_validator)

    def start(self):
        try:
            # self.para[1][0].setText('300')
            # self.para[2][0].setText('399')
            # self.para[3][0].setText('498')
            # self.para[4][0].setText('595')
            # self.para[5][0].setText('690')

            self.config = load_conf()
            self.index = self.config['index']
            self.num = fnum(self.config['code'])
            if not self.input_03.text():
                self.input_03.setText(self.num)
            self.features = []
            self.target = []
            self.t = []
            self.len_data = 5
            if not self.para[0][0].text():
                self.dcm = "0.00"
            else:
                self.dcm = self.para[0][0].text()
            for i in range(1, 9):
                self.para[i][3].setText('')
            for i in range(1, 9):
                if not self.para[i][0].text():
                    if i < 6:
                        self.para[i][0].setText('输入数据不完整')
                        return '输入数据不完整'
                if not self.para[i][2].text():
                    if i < 6:
                        self.para[i][2].setText('输入数据不完整')
                        return '输入数据不完整'
                else:
                    if not self.para[i][1].text():
                        self.t.append(60)
                    else:
                        self.t.append(float(self.para[i][1].text()))
                    self.target.append(float(self.para[i][2].text()))
                    self.features.append(float(self.para[i][0].text())/float(self.t[i-1]))
            self.intercept, self.coef, self.err = reg(
                self.features, self.t, self.target, self.dcm)
            self.formula = 'V实=%s+%s×V示' % (self.intercept, self.coef)
            savefig(float(self.intercept), float(
                self.coef), self.features, self.target)
            for i in range(1, 9):
                if self.para[i][0].text():
                    self.para[i][3].setText(self.err.pop(0))
                else:
                    self.para[i][3].setText('-')
        except Exception as e:
            print(repr(e))

    def generate(self):
        try:
            html = self.tohtml(self.config, self.formula)
            with open("app/temdata002.html", "w", encoding='utf-8')as htmlf:
                htmlf.write(html)
            reportWindow.__init__()
            reportWindow.show()
        except Exception as e:
            print(repr(e))
            alertWindow.__init__('请先执行校准！', '警告')
            alertWindow.show()

    def configuration(self):
        configWindow.__init__()
        configWindow.show()

    def about(self):
        content = """version:1.0

Copyright ©2020 DKC. All rights reserved.
        """
        alertWindow.__init__(content, '关于')
        alertWindow.show()

    def help(self):
        content = """使用帮助：

    1.输入精确度（选填，默认为0.00）。
        例：如需保留4位小数，输入0.0000。
    2.输入启动风速，单位为"m/s"。
    3.输入证书编号（选填，空缺则自动生成编号）。
    4.分别输入不少于5组测量点数据。
    5.点击开始校准计算非线性误差绝对值，单位为"m/s"。
    6.点击生成报告即可保存报告，存储路径为"report"文件夹。

"""
        helpWindow.__init__(content)
        helpWindow.show()

    def tohtml(self, config, formula):
        html_para = [
            self.input_03.text(),
            self.input_03.text(),
            self.input_02.text(),
            self.para[1][3].text(),
            self.para[2][3].text(),
            self.para[3][3].text(),
            self.para[4][3].text(),
            self.para[5][3].text(),
            self.para[6][3].text(),
            self.para[7][3].text(),
            self.para[8][3].text(),
            formula,
            encrypt.encrypt(config['para'], '16968', 0)
        ]
        html_text = """
                <!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <title>校准结果</title>
</head>
<style>
    .container {
        padding-top: 5px;
        width: 610px;
        height: 800px;
        margin-left: auto;
        margin-right: auto;
        border: 1px black solid;
        overflow: hidden;
    }

    .title {
        width: 500px;
        overflow: hidden;
        padding: 0;
        word-break: break-all;
        margin-left: auto;
        margin-right: auto;
        padding-top: 20px;
    }

    .title>h1 {
        text-align: center;
        line-height: 20px;
        padding-left: 20px;
        padding-right: 20px;
    }

    p {
        line-height: 12px;
        padding-left: 20px;
        padding-right: 20px;
    }

    .tab {
        width: 500px;
        padding: 0;
        word-break: break-all;
        margin-left: auto;
        margin-right: auto;
    }

    table {
        border-collapse: collapse;
        text-align: center;
        padding: 1px;
    }

    .figure {
        width: 500px;
        height: 350px;
        padding-left: 0px;
        padding-right: 0px;
    }

    .head {
        width: 120px;
        height: 30px;
    }

    .para {
        width: 60px;
        height: 30px;
    }

    p.footer {
        padding-top: 10px;
        text-align: center;
    }
</style>

<body>
    <div class="container">
        <div class="title">
            <h1>校准结果</h1>
            <h1>RESULTS OF CALIBRATIONS</h1>
        </div>
        <div class="tab">
            <p><strong>证书编号：%s</strong></h2>
            <p>Certificate No:%s</h2>
            <p>1、起动风速：%s m/s</p>
            <p>2、非线性误差的绝对值列表</p>
            <table border="1">
                <tr>
                    <td class="head">项目检测点</td>
                    <td class="para">1</td>
                    <td class="para">2</td>
                    <td class="para">3</td>
                    <td class="para">4</td>
                    <td class="para">5</td>
                    <td class="para">6</td>
                    <td class="para">7</td>
                    <td class="para">8</td>
                </tr>
                <tr>
                    <td class="head">非线性误差绝对值(m/s)</td>
                    <td class="para">%s</td>
                    <td class="para">%s</td>
                    <td class="para">%s</td>
                    <td class="para">%s</td>
                    <td class="para">%s</td>
                    <td class="para">%s</td>
                    <td class="para">%s</td>
                    <td class="para">%s</td>
                </tr>
            </table>
            <p>3.校准结果</p><img class="figure" src="temdata001">
            <p>校准曲线公式：%s</p>
        </div>
        <p class="footer">%s</p>
    </div>
</body>
<script>window.print()</script>

</html>
        """ % tuple((html_para))
        return html_text


class ConfigForm(QDialog, Ui_configwin):
    def __init__(self):
        super(ConfigForm, self).__init__()
        self.key = '16968'
        self.setupUi(self)
        input_reg = QtCore.QRegExp(r"[a-zA-Z0-9]{6}")
        input_validator = QtGui.QRegExpValidator(input_reg)
        inputc_reg = QtCore.QRegExp(r".{32}")
        inputc_validator = QtGui.QRegExpValidator(input_reg)
        self.code.setValidator(input_validator)
        self.company.setValidator(inputc_validator)
        config = load_conf()
        company_s = encrypt.encrypt(config['para'], self.key, 0)
        self.company.setText(company_s)
        self.code.setText(config['code'])

    def setConfig(self):
        set_conf(self.company.text(), self.code.text(),
                 self.pwd.text(), self.key)
        self.close()


class ReportForm(QDialog, Ui_reportwin):
    def __init__(self):
        super(ReportForm, self).__init__()
        self.setupUi(self)
        self.browser.load(QUrl('file:///app/temdata002.html'))

    def screen_shot(self):
        try:
            screen = QApplication.primaryScreen()
            winid = self.browser.winId()
            pix = screen.grabWindow(int(winid))
            config = load_conf()
            filename = fnum(config['code'])
            name = 'report/%s.png'%filename
            pix.save(name)
            alertWindow.__init__('文件保存位置：report/%s.是否直接打印？'%filename, '保存成功')
            alertWindow.buttonBox.accepted.connect(self.prt)
            alertWindow.show()
        except:
            alertWindow.__init__('保存失败！', '保存失败')
            alertWindow.show()
    def prt(self):
        
        try:
            system('cd app && temdata002.html')
        except:
            print('print err')


class AlertForm(QDialog, Ui_alertwin):
    def __init__(self, t, T):
        super(AlertForm, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(T)
        self.content.setText(t)


class HelpForm(QDialog, Ui_helpwin):
    def __init__(self, t):
        super(HelpForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(argv)
    win = MainForm()
    win.show()
    configWindow = ConfigForm()
    reportWindow = ReportForm()
    alertWindow = AlertForm('提示', '标题')
    helpWindow = HelpForm('帮助')
    exit(app.exec_())