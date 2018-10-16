# -*- coding:utf-8 -*-
"""
绘制并制定化图表
定义图表类型：柱状图、线形图、和堆积柱状图
"""

# 1------------------------
import matplotlib.pyplot as plt
# from matplotlib.pyplot import *
x = range(1, 5)
y = range(5, 1, -1)
# create new figure
plt.figure()
# dicide subplots into 2 * 3 grid, and select #1
plt.subplot(231)
plt.plot(x, y)

# select #2
plt.subplot(232)
plt.bar(x, y)
# horizontal bar-charts
plt.subplot(233)
plt.barh(x, y)

# create stacked bar charts
plt.subplot(234)
plt.bar(x, y)

# we need more data for stacked bar charts
# y1 = [7, 8, 5, 3]
y1 = [3, 5, 8, 7]
plt.bar(x, y1, bottom=y, color='r')     # bottom = y 底部等于 y

# box plot
plt.subplot(235)
plt.boxplot(x)

# scatter plot
plt.subplot(236)
plt.scatter(x, y)
plt.show()