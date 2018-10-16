# -*-coding:utf-8 -*-
"""
绘制极线图
    在极坐标系统中，点被描述为半径距离（通常表示为r）和角度（通常表示为theta）。
    角度可以用户弧度或者角度表示，但是matplotlib使用角度
    使用polar()函数绘制极线图。polor()函数接收两个相同长度的参数theta和r。
    函数也接收其他和plot()函数相同的格式化参数。
    使用matplotlib.pyplot.rgrids()来切换半径网格的显示或者设置标签
    使用matplotlib.pyplot.thetagrid（）来配置角度刻度与标签
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

figsize = 7
colormap = lambda r: cm.Set2(r/20.0)
N = 18  # number of bars

fig = plt.figure(figsize=(figsize, figsize))
"""创建正方形图表，并向其添加极限坐标轴"""
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7], polar=True)

theta = np.arange(0, 2 * np.pi, 2 * np.pi/N)
radii = 20 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = ax.bar(theta, radii, width=width, bottom=0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(colormap(r))
    bar.set_alpha(0.6)

plt.show()

"""
1、图表不必是正方形，但是如果不这样的话，极线图就是椭圆形（而不是圆形）的了
2、其次，为角度（theta）集合和极限距离（radii）生成随机值。因为绘制的是极限条，需要为每一个极限条提供宽度集合
3、因matplotlib.axes.bar接收值数组（几乎matplotlib中所有的绘图函数都是如此），所以不必在这个生成数据集合上做循环遍历，
而只需要调用一次bar函数，并传入所有参数
4、为了区分每一个极限条，需要循环遍历添加到ax（坐标轴）的每一个极限条，并制定化其外观
"""