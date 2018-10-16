# -*-coding:utf-8 -*-
"""
创建子区（subplots）
"""
import matplotlib.pyplot as plt

plt.figure(0)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2))
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=2)

# tidy up tick  labels size
all_axes = plt.gcf().axes
for axx in all_axes:
    for ticklabel in axx.get_xticklabels() + axx.get_yticklabels():
        ticklabel.set_fontsize(10)

plt.suptitle('Demo of subplot2grid')
plt.show()
"""
向subplot2grid方法传入形状参数、位置（loc）参数和可选的rowspan及colspan参数
这里一个重要的区别是位置从0开始索引，而figure.add_subplot从1开始索引。
"""