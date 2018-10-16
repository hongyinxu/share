# -*- coding:utf-8 -*-

"""
设置刻度、刻度标签和网格
使用 matplotlib.axes.Axes 类的坐标轴实例，这样可以把plot放置在图形窗口的任意位置
    1、tick locator ：指定刻度所在的位置
    2、tick formatter : 指定刻度显示的样式

使用matplotib.pyplot.locator_params() 方法控制刻度定位器行为
"""
from matplotlib import pyplot as plt
import numpy as np
# from pylab import *

# get current axis
ax = plt.gca()

# set view to tight, and maximum number of tick intervals(间隔) to 10
ax.locator_params(tight=True, nbins=10)

# generate 100 normal distribution values
ax.plot(np.random.normal(10, 0.1, 100))     # （10，0.1，100）平均值，标准差，数量
plt.show()