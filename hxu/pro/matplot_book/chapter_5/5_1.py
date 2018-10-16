# -*-coding:utf-8 -*-
"""
创建3D可视化图表
    1、创建3D柱状图
    2、创建3D直方图
    3、在matplotlib中创建动画
    4、用openGl制作动画

比较流行的工具包有Basemap, GTK工具、Excel工具、Natgrid工具、AxesGrid工具、和mplot3d
mpl_toolkits.mplot3工具提供了一些基本的3D绘图功能，其支持的图表类型包括散点图（scatter）、曲面图(surf)、线图（line）
和网格图（mesh）
虽然 mplot3D 不是一个最好的3D图形绘制库，但是它是伴随着matplotlob产生的

基本而言，我们仍然需要创建一个图表并把想要的坐标轴添加到上面，但不同的是我们为图表指定的是3D视图，添加坐标轴是Axes3D

函数mpl_toolkits.mplot3d.Axes3D.plot指定xs,ys,zs,zdir参数其他参数则直接传给matplotlib.axes.Axes.plot
    1、xs 和 ys ：x轴和y轴坐标
    2、zs：这是z轴的坐标值，可以是所有点对应的一个值，或者是每个点对应一个值
    3、zdir：决定那个坐标轴作为z轴的纬度（通常指zs，但也可以是xs、或者ys）
"""
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.size'] = 10

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for z in [2011, 2012, 2013, 2014]:
    xs = range(1, 13)
    # ys = 1 * np.random.normal(10, 1, (2, 3))      # rand() 产生0-1之间的随机数（产生均匀分布的样本值）,参数表数组大小
    ys = 1000 * np.random.rand(12)                  # randn() 产生正态分布（平均值0，标准差1）的样本值,参数表数组大小
    # print (ys)                          # randint()从给定的上下限范围内随机选取整数
                            # normal()产生正态高斯分布的样本值,第一个数时平均值，第二个数是标准差，最后一个是数组大小
    color = plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))
    ax.bar(xs, ys, zs=z, zdir='y', color=color, alpha=0.8)

ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))
ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))

ax.set_xlabel('Month')
ax.set_ylabel('Year')
ax.set_zlabel('Sales Net [usd]')
plt.show()