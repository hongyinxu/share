# -*-coding:utf-8 -*-
"""
绘制直方图
    1，一定间隔下数据点的频率的垂直矩形称为bin。bin以图固定的间隔创建，
        因此直方图的总面积等于数据点的数量
    2、bins ：可以是一个bin数量的整数值，也可以是表示bin的一个数列。默认值为10
    3、range:bin的范围，当bins参数为序列时。此参数无效。范围外的值将被忽略，默认值为None
    4、normed: 如果值为True，直方图将进行归一化（normalized）处理，形成概率密度，，默认值False
    5、histtype：默认为bar类型的直方图
        barstacked:用于多种数据的堆叠直方图
        step：创建为填充的线形图
        stepfilled:创建默认填充的线形图，
    6、align（对齐，使结盟）:用于bin边界之间的矩形条的居中设置。默认值是mid，（left,right）
    7、color指定直方图的颜色。（可以指定单一颜色或者颜色的序列），
        如果指定了多个数据集合，序列颜色将会设置为相同的序列（一一对应）
        如果未指定，将会使用一个默认的线条颜色
    8、orinetation:指定设置orientataion为horizontal创建水平直方图。默认vertical
"""
import numpy as np
import matplotlib.pyplot as plt
mu = 100
sigma = 15
x = np.random.normal(mu, sigma, 10000)

ax = plt.gca()

# the histogram of the data
# ax.hist(x, bins=35, color='k', normed=True, orientation='horizontal', histtype='step')
# ax.hist(x, bins=35, color='k', normed=True, orientation='horizontal', histtype='stepfilled')
ax.hist(x, bins=35, color='k', normed=True, orientation='horizontal', histtype='barstacked', align='right')

ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
ax.set_title(r'$\mathrm{Histogram:}\ \mu=%d,\ \sigma=%d$' % (mu, sigma))
plt.show()