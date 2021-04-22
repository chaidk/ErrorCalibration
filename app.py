import pandas as pd
import numpy as np
from pyecharts.types import Label
from scipy.sparse.linalg import interface
from sklearn.linear_model import LinearRegression
import pyecharts.options as opts
from pyecharts.render import make_snapshot
#from snapshot_phantomjs import snapshot
from pyecharts.charts import Line
from matplotlib import pyplot as plt
from decimal import Decimal


if __name__ == '__main__':
    features = np.array([300 ,399, 498, 595, 690]).reshape(-1,1)
    target = [2, 4, 6, 8, 10]
    features = features / 60
    dcm = '0.00'
            
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



    intercept, coef = reg()
    lerror = []
    for i in range(0,5):
        lerror.append(error(i))
    print(lerror)
    formula = '校准曲线公式： V实=%s+%s×V示'%(to_decimal(intercept, dcm), to_decimal(coef, dcm))
    print(formula)
'''
#绘图
    x_data = range(5,30,5)
    y_data = coef * x_data +intercept
    line = Line()
    (
        line
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="校准曲线",
            y_axis=y_data,
            symbol="emptyCircle",
            is_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=True),
            is_clip = True,
        )
        .render()
    )
print(line)
#make_snapshot(snapshot, line.render(), "report.png")

'''
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

plt.plot(x_data, y_data,Label='回归曲线')

plt.legend()

plt.show()
#加编号
#命名规则
#公司名称设置 加密算法https://blog.csdn.net/weixin_40406241/article/details/89321011
#帮助
#pdf https://blog.csdn.net/BobYuan888/article/details/108769274
