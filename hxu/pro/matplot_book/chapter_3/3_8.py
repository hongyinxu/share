# -*-coding:utf-8 -*-
"""
移动轴线到中央
隐藏两个轴（设置coloe 为none）
移动另外两个到坐标轴（0， 0）
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 500, endpoint=True)
y = np.sin(x)

plt.plot(x, y)
# get current axis
ax = plt.gca()

# hide two spines（脊柱）
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# move bottom and left spine to (0, 0)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# move ticks position
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()

"""
补充说明：轴线可以被限制在数据结束的地方
如：调用set_smart_bounds(True)。在这种情况下matplotlib会尝试以一种复杂的形式设置边界；
例如处理颠倒的边界，或者在数据延伸出视图的情况下裁剪线条以适应视图
"""
