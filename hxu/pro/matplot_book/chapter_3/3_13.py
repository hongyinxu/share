# -*-coding:utf-8 -*-
"""
绘制带彩色标记的散点图
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y1 = np.random.randn(len(x))
y2 = 1.2 + np.exp(x)

ax1 = plt.subplot(121)
plt.scatter(x, y1, color='indigo', alpha=0.3, edgecolors='white', label='no correlation')
plt.xlabel('no correlation')
plt.grid(True)
plt.legend(loc='upper left')

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
plt.scatter(x, y2, color='green', alpha=0.3, edgecolors='grey', label='correlation')
plt.xlabel('strong correlation')
plt.grid(True)
plt.legend()

plt.show()