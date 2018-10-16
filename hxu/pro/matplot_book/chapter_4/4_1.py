# -*-coding:utf-8 -*-
"""
matplotlib 最上层时一个Figure 实例。
Figure 实例包含了一个Axes实例字段 Figure.axes。Axes包含几乎所有我们关心的额东西（线，点，刻度，标签）
因此，当调用plot()方法时，就会向Axes.lines列表添加一个线条的实例（matplotlib.lines.Line2D）
如果绘制一个直方图（hist）,就会向Axes.patches列表添加许多矩形
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects
"""
1、创建一个基于一些随机生成的数据的plot
2、添加title、和axes标签
3、添加alpha设置
4、向title 和 axes 标签添加阴影效果
"""

data = np.random.randn(70)
fontsize = 18
plt.plot(data)

title = "This is figure title"
x_label = 'This is x axis title'
y_label = 'This is y axis title'

title_text_obj = plt.title(title, fontsize=fontsize, verticalalignment='bottom')

title_text_obj.set_path_effects([patheffects.withSimplePatchShadow()])

# offset_xy -- set the 'angle' of the shadow
# shadow_rgbFace -- set the color of the shadow
# patch_alpha -- setup the transparency of the shadow

offset_xy = (1, -1)
rgbRed = (1, 0, 0)
alpha = 0.8

# customize shadow properties
pe = patheffects.withSimplePatchShadow(offset=offset_xy,
                                       shadow_rgbFace=rgbRed,
                                       alpha=alpha)

# apply them to the xais and yaxis labels

xlabel_obj = plt.xlabel(x_label, fontsize=fontsize, alpha=0.5)
xlabel_obj.set_path_effects([pe])

ylabel_obj = plt.ylabel(y_label, fontsize=fontsize, alpha=0.5)
ylabel_obj.set_path_effects([pe])

plt.show()