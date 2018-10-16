# -*-coding:utf-8 -*-
"""
以另一种方式定制化当前的axes或者subplot的例子
"""
import matplotlib.pyplot as plt
import matplotlib
fig = plt.figure()
axes = fig.add_subplot(111)
rectangle = axes.patch
rectangle.set_facecolor('blue')

# rect = matplotlib.patches.Rectangle((1, 1), width=6, height=12)
# rect.set_facecolor('blue')
# axes.add_patch(rect)

# we have to manually force a figure draw
axes.figure.canvas.draw()
plt.show()