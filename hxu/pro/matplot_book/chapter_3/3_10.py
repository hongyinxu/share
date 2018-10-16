# -*-coding:utf-8 -*-
"""
绘制误差条形图
    可以y用误差条来来可视化数据集合中的测量不确定度，或者指出误差
    1、width：给定误差条的宽度，默认值0.8
    2、bottom:如果指定了bottom，其值会加到高度中，默认值为None
    3、edgecolor：给定误差条边界颜色
    4、linewidth：误差条边界宽度，可以设为None(默认值)和0（此时误差条不显示）
    5、orientation：有vertical 和 horizontal
    6、xerr和yerr:用于在柱状图上生成误差条
    注：一些可选参数（color,edgecolor,linewidth,xerr,yerr）
    可以是单一值，也可以是和误差条数，相同的序列
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10, 1)

y = np.log(x)

# add some error samples from standard noemal distribution
xe = 0.1 * np.abs(np.random.randn(len(y)))
xe1 = -0.1 * np.abs(np.random.randn(len(y)))

# plt.bar(x, y, yerr=xe, xerr=xe, width=0.4, align='center',
#         ecolor='r', color='cyan', label='experiment #1')

plt.bar(x, y, yerr=[xe1, xe], xerr=xe, width=0.4, align='center',
        ecolor='r', color='cyan', label='experiment #1')

# give some explainations
plt.xlabel('# measurement')
plt.ylabel('Measured values')
plt.title('Measurements')
plt.legend(loc='upper left')

plt.show()

"""
上述用到的误差条为对称误差条。如果数据集合的性质是误差在两个方向上不同，可使用非对称误差条。
非对称误差条必须用一个两个元素的列表（比如一个二维数组）来指定xerr, 
其中第一个列表包含负向误差的值，第二个包含正想误差的值
"""