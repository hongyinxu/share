# -*- coding:utf-8 -*-
"""
绘制箱线图和直方图
"""
from matplotlib import pyplot as plt

dataset = [113, 115, 119, 121, 124,
           124, 125, 126, 126, 126,
           127, 127, 128, 129, 130,
           130, 131, 132, 133, 136
           ]
plt.subplot(121)
plt.boxplot(dataset, vert=False)    # vert代表vertical
plt.subplot(122)
plt.hist(dataset)
plt.show()