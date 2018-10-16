# -*-coding:utf-8 -*-
"""
创建等高线图：等高线图显示的是矩阵的等值线（isolines），
等值线使用数值相等个点连成的曲线。（数值通过一个有两个参数的函数获得）

Z矩阵的等高线图由许多等高线表示，Z被视为相对于X-Y平面的高度。
Z的最小值为2，并且必须包含至少两个不同的值
等高线图的缺陷：
    如果在编码时不为等值线添加标签，它将毫无意义，因为我们不能分辨最高点和最低点，或者找出局部极小值
    可以使用标签（clabel()）或者colormaps为等值线添加标签。如果你的输出媒介允许使用颜色，首先colormaps
等高线的另一个风险是如何选择要绘制的等值线数量。太多：图标太密集，难以理解；太少：丢失信息，不便理解数

函数contour（）会自动猜测出将绘制出多少等值线，我们也可指定数量
    contour()绘制等高线
    contourf()绘制填充等高线

调用签名：
    contour(Z):          绘制Z（数组）的等高线。自动选择水平值
    contour(X,Y,Z)：     绘制X、Y和Z的等高线。X、Y数组为（X、Y）平面坐标（surface coordinates）
    contour(Z,N):        绘制Z的等高线图，其中水平数由N决定。自动选择水平值
    contour(X,Y,Z,N)：   绘制Z的等高线图，其中水平数由N决定。自动选择水平值
    contour(Z,V)：       绘制等高线，水平值在V中指定
    contour(X,Y.Z.V)：   绘制等高线，水平值在V中指定
    contour(...,V)：     填充V序列中的水平值之间的len(V)-1个区域
    contour(Z, **kwargs)：使用关键字参数控制一般线条属性（颜色、线宽、起点、颜色映射表（colormap）等）
    X、Y和Z的形状和纬度存在一定的限制。
        X、Y可以是二维的，与Z形状相同
        如果他们是一维的，则X的长度等于Z的列数，Y的长度等于Z的函数

"""

"""
1、实现一个方法来模拟信号处理器
2、生成一些线性信号数据
3、把数据转换到合适的矩阵中供矩阵操作使用
4、绘制等高线图
5、添加等高线标签
6、显示图形
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def process_signals(x, y):
    return (1-(x ** 2 + y ** 2)) * np.exp(-y ** 3 /3)


x = np.arange(-1.5, 1.5, 0.1)
y = np.arange(-1.5, 1.5, 0.1)

# make grids of points
X, Y =np.meshgrid(x, y)
Z = process_signals(X, Y)

# number of isolines
# N = np.arange(-1, 1.5, 0.5)
N = np.arange(-1, 1.5, 0.3)

# adding the contour lines with labels
CS = plt.contour(Z, N, linewidths=2, cmap=mpl.cm.jet)
# CS = plt.contourf(Z, N, linewidths=2, cmap=mpl.cm.jet)
plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(CS)

plt.title("My function: $z=(1-x^2+y^2) e^{-(y^3)/3}$")
plt.show()

"""通过简单的传入一个CS（matplotlib.contour.QuadContourSet实例），向图表添加了一个颜色映射表"""
