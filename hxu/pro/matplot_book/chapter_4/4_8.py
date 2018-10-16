# -*-coding:utf-8 -*-
"""
填充图标底层区域
在matplotlib中绘制一个填充多边形的基本方式是使用matplotlib.pyplot.fill
该方法接收和matplotlib.pyplot.plot相似的参数，即多个x、y对和其他Line2D属性
函数返回被添加的的Patch实例的列表
"""

"""
填充两条曲线之间的额多边形：matplotlib.pyplot.fill, matplotlib.pyplot.fill_between(), matplotlib.pyplot.fill_betweenx()
fill_between()填充y轴的值级之间的区域
fill_betweenx()填充x轴的值之间的区域

函数fill_between接收参数x(数据的x轴数组)和y1及y2(数据的y轴数组)。通过参数，可以指定条件来决定要填充的区域
这个条件是一个布尔条件，通常指定y轴的范围。
默认值是None，表示填充所有的区域
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

t = range(1000)
y = [sqrt(i) for i in t]

plt.plot(t, y, color='red', lw=2)       # lw 表示linewidth
plt.fill_between(t, y, color='silver')
plt.show()