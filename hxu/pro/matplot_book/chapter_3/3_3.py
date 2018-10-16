# -*- coding:utf-8 -*-
"""
简单正弦图和余弦图，示例：数学表达式写法
"""
from matplotlib import pyplot as plt
import matplotlib.lines as line
# from pylab import *
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.cos(x)

y1 = np.sin(x)

lines, = plt.plot(x, y)
line.Line2D.set_dashes(lines, [1, 1])
plt.plot(x, y1)

# define plot title
plt.title("Functions $\sin$ and $\cos$")

# set x limit 貌似没起到作用
plt.xlim = (-1, 1)
# set y limit
plt.ylim = (-1, 1)
"""$-pi$ , 表示在图表中写上希腊字母，称作 LaTex 语法"""
# format ticks at specific values
# xt = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
# xtl = [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+pi/2$', r'$pi$']
# yt = [-1, 0, 1]
# ytl = [r'$-1$', r'$0$', r'$+1$']
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+pi/2$', r'$pi$'])
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])
# plt.xticks(xt, xtl)
# plt.yticks(yt, ytl)
# plt.axhline(y=0.5)
# plt.axvline(x=0.5)
# plt.axvspan(xmin=0, xmax=1)
# plt.axhspan(ymin=0, ymax=1)
# plt.da
plt.show()

# 22 ------------------------------------------------------------------------
# from matplotlib import pyplot as plt
# from pylab import *
# import numpy as np
#
# x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# y = np.cos(x)
#
# y1 = np.sin(x)
#
# plot(x, y)
# plot(x, y1)

# define plot title
# title("Functions $\sin$ and $\cos$")

# set x limit 貌似没起到作用
# xlim = (-1, 1)
# # set y limit
# ylim = (-1, 1)
"""$-pi$ , 表示在图表中写上希腊字母，称作 LaTex 语法"""
# format ticks at specific values
# xt = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
# xtl = [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+pi/2$', r'$pi$']
# yt = [-1, 0, 1]
# ytl = [r'$-1$', r'$0$', r'$+1$']
# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+pi/2$', r'$pi$'])
# yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])
# plt.xticks(xt, xtl)
# plt.yticks(yt, ytl)
# show()