# -*-coding:utf-8 -*-
"""
向图表添加数据表
"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
ax = plt.gca()
y = np.random.randn(9)

col_labels = ['col1', 'col2', 'col3']
row_labels = ['row1', 'row2', 'row3']
tabel_vals = [[11, 12, 13], [21, 22, 23], [28, 29, 30]]
row_colors = ['red', 'gold', 'green']
my_tabel = plt.table(cellText=tabel_vals, colWidths=[0.1] * 3, rowLabels=row_labels,
                     colLabels=col_labels, rowColours=row_colors, loc='upper right')
plt.plot(y)
# plt.show()

"""
基本的函数签名如下：
    table(cellText=None, cellColours=None, cellLoc='right',
            colWidths=None, colLabels=None,colColours=None, colLoc='center',
            rowLabels=None, rowColours=None, rowLoc='left',
            loc='bottom', bbox=None)
"""
# ax.add_table(my_tabel)
plt.show()

"""
可以使用Axes.add_table(table)方法把table实例添加岛axes,这里的table是matplotlib.table.Table类的实例
"""
