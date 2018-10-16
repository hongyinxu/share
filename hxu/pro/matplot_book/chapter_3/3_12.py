# -*-coding:utf-8 -*-
"""
绘制带填充区域的图表
"""

from matplotlib.pyplot import figure, show, gca
import numpy as np

x = np.linspace(0, 2, 200)
# two different signals are measured
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)

fig = figure()
ax = gca()

# plot and fill between y1, y2, where a logical condition is met
ax.plot(x, y1, x, y2, color='black')
# ax.plot(x, y1, x, y2)
ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='darkblue', interpolate=True)
ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='deeppink', interpolate=True)

ax.set_title('filled between')

show()
