import pandas as pd
import numpy as np
import os, json
from scipy.sparse.linalg import interface
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from decimal import Decimal

import encrypt， ini


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

def reg():
    model = LinearRegression()
    model.fit(features, target)
    intercept = model.intercept_ 
    coef = model.coef_[0]
    print(to_decimal(intercept, dcm), to_decimal(coef, dcm))
    return intercept, coef

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
        if fname.find('td'):
            num+=1
    fnum = td + '%02d'%num
    return fnum


if __name__ == '__main__':
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
    index = conf['index']
    
    
    fname = fnum()
    print(fname)



#加编号
#命名规则
#公司名称设置 加密算法https://blog.csdn.net/weixin_40406241/article/details/89321011
#帮助
#pdf https://blog.csdn.net/BobYuan888/article/details/108769274
