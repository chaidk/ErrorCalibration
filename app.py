from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot,  QUrl
from PyQt5 import QtGui
from numpy.lib.function_base import append, percentile
from Ui_MainWindow import Ui_MainWindow,QtCore

import pandas as pd
import numpy as np
import sys, os, json, datetime
from scipy.sparse.linalg import interface
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from decimal import Decimal

import encrypt
def load_conf():
    with open('config.json', 'r', encoding='utf8') as fp:
        conf = json.load(fp)
        return conf
def set_conf(conf):
    with open('config.json', 'w', encoding='utf8') as fp:
        conf = json.dump(conf, fp, ensure_ascii=False)
def set_company(name):
    conf =load_conf()
    conf['company'] = name
    set_conf(conf)
        
def to_decimal(num, exp="0.00") -> Decimal:
    if not num:
        return Decimal("0").quantize(exp=Decimal(exp))
    if not isinstance(num, str):
        num = str(num)
    return Decimal(num).quantize(exp=Decimal(exp))

def reg(features, time, target, dcm):
    err = []
    model = LinearRegression()
    features = [a/b for a,b in zip(features, time)] 
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

def error(x):
    y = coef * features[x][0] + intercept
    err =  abs((y - target[x]))
    err = str(to_decimal(err, dcm))
    return err

def savefig():
    x_data = range(1,31,5)
    y_data = coef * x_data +intercept
    plt.figure('Grid', figsize = (6,6),dpi = 100)
    plt.title("校准曲线",fontsize=20, fontproperties="SimHei")
    plt.xlabel("风表示值Vz（格） ",fontsize=14, fontproperties="SimHei")
    plt.ylabel("实际风速值Vs（m/s)",fontsize=14, fontproperties="SimHei")
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(5.0))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    #紧凑布局
    plt.tight_layout()
    ax.grid(which='major',axis="both",linewidth=0.25,linestyle='-',color='gray')
    ax.grid(which='minor',axis="both",linewidth=0.25,linestyle='-',color='gray')
    plt.plot(x_data, y_data)
    plt.legend()
    plt.savefig('plt.png')
    plt.show()

def fnum():
    num = 1
    td = datetime.datetime.today().strftime('%Y%m%d')
    flist = os.listdir('report')
    for fname in flist:
        if fname[0:8].find(td) is not -1:
            num+=1
    fnum = 'JZFB' + td + '%02d'%num
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
            num = fnum()
            self.input_03.setText(num)
            features = []
            target = []
            time = []
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
                    if i < 6:
                        self.para[i][0].setText('输入数据不完整')
                        return False
                    
                else:
                    features.append(float(self.para[i][0].text()))
                    if not self.para[i][1].text():
                        time.append(60)
                    else:
                        time.append(float(self.para[i][1].text()))

                    if not self.para[i][2].text():
                        target.append(i*2)
                    else:
                        target.append(float(self.para[i][2].text()))
                
            print(features, target)
            intercept, coef, err = reg(features, time, target, dcm)
            #self.para[1][3].setText(str(intercept))
            #self.para[2][3].setText(str(coef))
            for i,e in enumerate(err):
                self.para[i+1][3].setText(e)
            for i in range(1,9):
                try:
                    self.para[i][3].setText(err[i-1])
                except:
                    self.para[i][3].setText('-')






            
                    
                
        except Exception as e:
            # self.intercept.setText(str(e))
            # self.coef.setText(repr(e))
            print(repr(e))

    def generate(self):
        pass



if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())



















    
    features = np.array([300 ,399, 498, 595, 690]).reshape(-1,1)
    target = [2, 4, 6, 8, 10]
    features = features / 60
    dcm = '0.00'
    


    intercept, coef = reg()
    lerror = []
    for i in range(0,5):
        lerror.append(error(i))
    print(lerror)
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

#序号
    conf = load_conf()
    
    
    fname = fnum()
    print(fname)



#加编号
#命名规则
#公司名称设置 加密算法https://blog.csdn.net/weixin_40406241/article/details/89321011
#帮助
#pdf https://blog.csdn.net/BobYuan888/article/details/108769274
#图标