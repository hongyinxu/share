# -*-coding:utf-8 -*-
"""
向图表添加阴影效果
使用matplotlib内置的transformation框架，其位于matplotlib.transforms模块中
transformations 知道如何将给定的坐标从其他坐标系转换到显示的坐标系中
    也知道如何将坐标系从显示坐标系转换到他们自己的坐标系中
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms


def setup(layout=None):
    assert layout is not None

    fig = plt.figure()
    ax = fig.add_subplot(layout)
    return fig, ax


def get_signal():
    t = np.arange(0, 2.5, 0.01)
    s = np.sin(5 * np.pi * t)
    return t, s


def plot_signal(t, s):
    line, = ax.plot(t, s, linewidth=5, color='magenta')
    return line,


def make_shadow(fig, axes, line, t, s):
    delta = 2/72.0  # how many points to move the shadow
    offset = transforms.ScaledTranslation(delta, -delta, fig.dpi_scale_trans)
    offset_transform = ax.transData + offset

    """we plot the same data, but now using offset transforms"""
    """zorder -- to render it below the line"""
    ax.plot(t, s, linewidth=5, color='grey', transform=offset_transform,
              zorder=0.5 * line.get_zorder())


if __name__ == '__main__':
    fig, ax = setup(111)
    t, s =get_signal()
    line, = plot_signal(t, s)

    make_shadow(fig, ax, line, t, s)
    ax.set_title('Shadow effect using an offset transform')
    plt.show()
    
"""
matplotlib包含一个transformations helper ——matplotlib.transforms.ScaledTranslation-添加偏移转换
dx, dy 的值以点为单位。因为点是1/27英寸，向右、向下移动偏移2pt
使用matplotlib.transforms.ScaledTransformation(xtr, ytr, scaletr)
    xtr, ytr 是转换的偏移量
    scaletr 是一个可转换可调用对象（callable）
    
"""