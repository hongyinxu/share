# -*- coding:utf-8 -*-
"""
添加图例和注解
"""
from matplotlib import pyplot as plt
import numpy as np

# generate different normal distributions
x1 = np.random.normal(30, 3, 100)
x2 = np.random.normal(20, 2, 100)
x3 = np.random.normal(10, 3, 100)

# plot them
plt.plot(x1, label='plot')
plt.plot(x2, label='2nd plot')
plt.plot(x3, label='last plot')

# generate a legend box
plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc='lower left', ncol=3, mode='expand', borderaxespad=0)
plt.annotate('Important value', (55, 20), xycoords='data', xytext=(5, 36), arrowprops=dict(arrowstyle='->'))

plt.show()

"""
1, 每个plot指定了一个字符串标签，这样legend()会吧他们添加岛图例框中
2、loc 指定图例框的位置（upper, lower, right, left, center）
3、ncol 是指图例列数为3
4,、指定边界框（bbox_to_anchor）的起始位置为（0，1.02），设置宽、高（1，0.102），这些值都是归一化轴坐标系
5、mode 参数（None 或 expand）当为expand时，图例框会扩张至整个坐标轴区域
6、borderaxespad 指定了坐标轴与图例边界之间的距离

7、（55,20）为xy坐标中的位置
8、xycoord='data' : 指定注解与数据使用相同的坐标系
9、xytext : 注解文本的起始位置
10、箭头由xytext指向xy坐标位置。arrowprops 字典中定义了很多箭头属性。在这里使用arrowstyle来指定箭头的风格
"""