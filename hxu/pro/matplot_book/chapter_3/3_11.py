# -*-coding:utf-8 -*-
"""
绘制饼图
饼图描述数值的比例关系，其中每个扇区的弧长大小为其所表示的数量的比例
1,autopct: 格式化绘制在圆弧中的标签，标签可以是一个格式化字符串或者一个可调用的对象（函数）
"""
# 绘制一个分裂式饼图
import matplotlib.pyplot as plt

""" make a square figure and axes"""
# plt.figure(1, figsize=(3, 3), dpi=300, facecolor='w', edgecolor='r')
plt.figure(1, figsize=(6, 6))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

# the slices will be ordered
# plotted counter-clockwise
labels = 'spring', 'summer', 'autumn', 'winter'

# fractions are either x/sum(x) or x if sum(x)<=1
x = [15, 30, 45, 10]

# explode must be len(x) sequence or None
explode = [0.1] * 4
plt.pie(x, explode=explode, labels=labels, autopct='%1.1f%%', startangle=67)
plt.title('Rainy days by season')
plt.show()