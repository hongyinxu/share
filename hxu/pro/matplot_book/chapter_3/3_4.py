# -*- coding:utf-8 -*-
"""
设置坐标轴长度和范围
    1、autoscale()(matplotlib.pyplot.autoscale())方法，该方法会计算坐标轴的最佳大小以适应数据的显示
    2、matplotlib.pyplot.axes()方法，向相同图形添加新的坐标轴
        rect 归一化单位（0， 1）下的 left, bottom, width, height
        axisbg :指定坐标轴的背景颜色
    3、matplotlib.pyplot.axhline(y=value) # 接收一个参数 ：y=value
    4、matplotlib.pyplot.axvline(x=value) 根据给定的x和y值相应的绘制出相对于坐标轴的水平线和垂直线
    5、matplotlib.pyplot.axhspan(ymin=value, ymax=value) 接收两个参数：ymin=value, ymax=value
    6、matplotlib.pyplot.axvspan(xmin=value, xmax=value) 绘制面积
    7，matplotlib.pyplot.grid() 控制网格
        参数 which : 指定绘制的网格刻度类型 （major, minor, both）
        参数 axis: 指定绘制哪组网格线 （both, x, y）
    matplotlib.lines.Line2D
        8、alpha [浮点数] 用于设置混色（透明度）
        9、dashes（破折号） [以点为单位的on/off序列]
        10、label [字符串]  为图例设置标签值r
        11、marker []     设置线条标记
        12、color [任意matplotlib颜色]   设置线条颜色
        13、linestyle 或 ls []     设置线条风格
        14、linewidth 或 lw [以点为单位的浮点值]    设置以点为单位的线宽
        15，markeredgecolor 或 mec [任意matplotlib颜色]   设置标记的边缘颜色
        16、markeredgewidth 或 mew [以点为单位的浮点值]    设置以点为单位的标记边缘宽度
        17、markerfacecolor 或 mfc [意matplotlib颜色]    设置标记的颜色
        18、markersize 或 ms  [浮点值]   设置以点为单位的标记大小
        19、solid_joinstyle ['button'|'round'|'projecting']  设置实线的线端风格
        20、solid_joinstyle ['miter',|'round'|'bevel']   设置实线的连接风格
        21、visible [Ture | False]   显示或隐藏artist
        22、xdata [np.array]     设置x的 np.array
        23、ydata [np.array]     设置 y 的 np.array
        24、zorder [任意数字]

"""