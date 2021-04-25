from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot,  QUrl, QSizeF
from PyQt5 import QtGui
from PyQt5.QtPrintSupport import QPrinter
from numpy.lib.function_base import append, percentile
from Ui_MainWindow import Ui_MainWindow,QtCore
from Ui_config import Ui_configwin,QtCore
from Ui_report import Ui_reportwin,QtCore

import pandas as pd
import numpy as np
import sys, os, json, datetime, time
from scipy.sparse.linalg import interface
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from decimal import Decimal

import encrypt

# def html_print(browser):
#     printer = QPrinter()
#     printer.setPageSizeMM(QSizeF(750, 1050))
#     browser.page().print(printer, print_compele())

# def print_compele():
#     print('print_compele')

def load_conf():
    with open('config.json', 'r', encoding='utf8') as fp:
        conf = json.load(fp)
        return conf
def set_conf(company, code, pwd):
    conf =load_conf()
    conf['para'] = company
    conf['code'] = code
    if pwd == 'pwd16968':
        with open('config.json', 'w', encoding='utf8') as fp:
            conf = json.dump(conf, fp, ensure_ascii=False)
            print('修改完成')
    else:
        print('密码错误')
        
def to_decimal(num, exp="0.00") -> Decimal:
    if not num:
        return Decimal("0").quantize(exp=Decimal(exp))
    if not isinstance(num, str):
        num = str(num)
    return Decimal(num).quantize(exp=Decimal(exp))

def reg(features, t, target, dcm):
    err = []
    model = LinearRegression()
    features = [a/b for a,b in zip(features, t)] 
    df_features = pd.DataFrame(features).values.reshape(-1, 1)
    df_target = pd.DataFrame(target)
    model.fit(df_features, df_target)
    intercept = float(model.intercept_)
    coef = float(model.coef_[0])
    for i,x in enumerate(features):
        y = coef * x + intercept
        e = abs((y - target[i]))
        print(i,x,e)
        e = str(to_decimal(e, dcm))
        err.append(e)
    #print(to_decimal(intercept, dcm), to_decimal(coef, dcm), err)
    return to_decimal(intercept, dcm), to_decimal(coef, dcm), err


def savefig(coef, intercept):
    x_data = range(1,31,5)
    y_data = [coef * x +intercept for x in x_data]
    plt.clf()
    plt.figure('Grid', figsize = (6,6),dpi = 100)
    plt.title("校准曲线",fontsize=20, fontproperties="SimHei")
    plt.xlabel("风表示值Vz（格） ",fontsize=14, fontproperties="SimHei")
    plt.ylabel("实际风速值Vs（m/s)",fontsize=14, fontproperties="SimHei")
    plt.yticks(y_data)
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(20.0))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
    
    #紧凑布局
    plt.tight_layout()
    ax.grid(which='major',axis="both",linewidth=0.25,linestyle='-',color='gray')
    ax.grid(which='minor',axis="both",linewidth=0.25,linestyle='-',color='gray')
    plt.plot(x_data, y_data)
    plt.legend()
    plt.savefig('tem/plt.png')


def fnum(code):
    num = 1
    td = datetime.datetime.today().strftime('%Y%m%d')
    flist = os.listdir('report')
    for fname in flist:
        if fname[0:8].find(td) is not -1:
            num+=1
    fnum = code + td + '%02d'%num
    return fnum
class MainForm(QMainWindow,Ui_MainWindow):
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
        int_reg = QtCore.QRegExp(r"[0-9]{6}")
        float_reg = QtCore.QRegExp(r"[0-9]{1,4}\.[0-9]{4}")
        input_reg = QtCore.QRegExp(r"[a-zA-Z0-9]{16}")
        dcm_validator = QtGui.QRegExpValidator(dcm_reg)
        int_validator = QtGui.QRegExpValidator(int_reg)
        float_validator = QtGui.QRegExpValidator(float_reg)
        input_validator = QtGui.QRegExpValidator(input_reg)
        self.para[0][0].setValidator(dcm_validator)
        self.para[0][1].setValidator(float_validator)
        self.para[0][2].setValidator(input_validator)
        for i in range(1,9):
            self.para[i][0].setValidator(float_validator)
            self.para[i][1].setValidator(int_validator)
            self.para[i][2].setValidator(int_validator)

    def start(self):
        try:
            config = load_conf()
            index = config['index']
            num = fnum(config['code'])
            if not self.input_03.text():
                self.input_03.setText(num)
            features = []
            target = []
            t = []
            len_data = 5
            if not self.para[0][0].text():
                dcm = "0.00"
            else:
                dcm = self.para[0][0].text()
            for i in range(1,9):
                self.para[i][3].setText('')
            for i in range(1,9):
                print(features)
                if not self.para[i][0].text():
                    if i < 3:
                        self.para[i][0].setText('输入数据不完整')
                        return '输入数据不完整'
                    
                else:
                    features.append(float(self.para[i][0].text()))
                    if not self.para[i][1].text():
                        t.append(60)
                    else:
                        t.append(float(self.para[i][1].text()))

                    if not self.para[i][2].text():
                        target.append(i*2)
                    else:
                        target.append(float(self.para[i][2].text()))
                
            print(features, target)
            intercept, coef, err = reg(features, t, target, dcm)
            formula = 'V实=%s+%s×V示'%(intercept, coef)
            savefig(float(intercept), float(coef))
            for i in range(1,9):
                if self.para[i][0].text():
                    self.para[i][3].setText(err.pop(0))
                else:
                    self.para[i][3].setText('-')
            
            html = self.tohtml(config, formula)
            with open("tem/tem", "w", encoding='utf-8')as htmlf:
                htmlf.write(html)
                
            reportWindow.__init__()
            reportWindow.show()

        except Exception as e:
            print(repr(e))

    def generate(self):
        pass

    def configuration(self):
        configWindow.__init__()
        configWindow.show()

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
        config['para']
        ]
        print(html_para)
        html_text = """
                <!DOCTYPE html>
                <html lang="zh-CN">
                <head>
                    <meta charset="utf-8">
                    <title>校准结果</title>
                </head>
                <style>
                    .container{
                        width: 700px;
                        /* height: 1123px; */
                        height: 1000px;
                        margin-left: auto;
                        margin-right: auto;
                        border: 1px black solid;
                        overflow: hidden;
                    }
                    .title{
                        width: 600px;
                        overflow: hidden;
                        padding: 0;
                        word-break:break-all;
                        margin-left: auto;
                        margin-right: auto;
                        padding-top: 50px;
                    }
                    .title>h1{
                        text-align: center;
                        line-height: 20px;
                        padding-left: 20px;
                        padding-right: 20px;
                    }

                    p{
                        line-height: 15px;
                        padding-left: 20px;
                        padding-right: 20px;
                    }
                    .tab{
                        width: 600px;
                        padding: 0;
                        word-break:break-all;
                        margin-left: auto;
                        margin-right: auto;
                    }
                    table{
                        border-collapse: collapse;
                        text-align: center;
                        padding: 2px;
                    }
                    .figure{
                        width: 500px;
                        height: 500px;
                        padding-left: 50px;
                        padding-right: 50px;
                        
                    }
                    .head{
                        width: 120px;
                        height: 40px;
                    }
                    .para{
                        width: 60px;
                        height: 40px;
                    }
                    footer{
                        text-align: center;
                    }
                </style>
                <body>
                    <div class="container">
                        <div class="title">
                            <h1>校准结果</h1>
                            <h1>RESULTS OF CALIBRATIONS</h1>
                            <p><strong>证书编号：%s</strong></h2>
                            <p>Certificate  No:%s</h2>
                            <p>1、起动风速：%s m/s</p>
                            <p>2、非线性误差的绝对值列表</p>
                                
                        </div>
                        <div class="tab">
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
                            <p>3.校准结果</p>
                            <img class="figure" src="plt.png">
                            <p>校准曲线公式：%s</p>
                        </div>
                        <footer>
                            <b>%s</b>
                        </footer>
                    </div>

                </body>
                </html>
        """%tuple((html_para))
        return html_text


class ConfigForm(QDialog,Ui_configwin):
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
        set_conf(self.company.text(), self.code.text(), self.pwd.text())





class ReportForm(QDialog,Ui_reportwin):
    def __init__(self):
        super(ReportForm, self).__init__()
        self.setupUi(self)
        #time.sleep(1)
        #self.screen_shot()
        self.browser.load(QUrl('file:///tem/tem'))
    def screen_shot(self):
        screen = QApplication.primaryScreen()
        winid = self.browser.winId()
        pix = screen.grabWindow(int(winid))
        print(int(winid))
        name = 'scr.png'
        pix.save(name)



if __name__ == '__main__':
    
    global html
    app = QApplication(sys.argv)
    win = MainForm()
    configWindow = ConfigForm()
    reportWindow = ReportForm()
    win.show()
    sys.exit(app.exec_())

    formula = '校准曲线公式： V实=%s+%s×V示'%(to_decimal(intercept, dcm), to_decimal(coef, dcm))
    print(formula)
    #savefig()

#加密
    company = '临汾开成设备检测有限公司'
    key = '16968'
    company_h = encrypt.encrypt(company, key, 1)
    print(company_h)
    set_company(company_h)

    company_s = encrypt.encrypt(load_conf()['company'], key, 0)
    
    print(company_s)
#测量点 报告
#~加编号
#~命名规则
#~公司名称设置 加密算法https://blog.csdn.net/weixin_40406241/article/details/89321011
#帮助
#pdf https://blog.csdn.net/BobYuan888/article/details/108769274
#图标