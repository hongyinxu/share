# -*- coding:utf-8 -*-
"""
1、在代码中配置matplotlib参数
    （1）通过 rcParams 字典访问并修改所有已经加载的配置项
    （2）通过向 matplotlib.rc() 传入属性的关键字元组来修改配置项
        import matplotlib as mpl
        mpl.rcParams['lines.linewidth'] = 2
        mpl.rcParams['lines.color'] = 'r'

        import matplotlib as mpl
        mpl.rc('lines', linewith=2, color='r')
        如果需要重置设置，需要调用 matplotlib.rcdefaults() 方法

"""
import matplotlib as mpl

"""
配置文件包括以下配置：
    1、axes: 设置坐标轴边界和表面的颜色、坐标轴刻度大小和网格显示
    2、backend : 设置目标输出 TKAgg 和 GTKAgg
    3、figure ：控制 dpi 、 边界颜色、图形大小、和子区（subplot）设置
    4、font ：字体集（font family）、字体大小 和样式设置
    5、grid：设置网格颜色和线条
    6、legend ： 设置图例和图中文本显示
    7、line ： 设置线条（颜色、线型、宽度等）和标记
    8、patch : 时填充的2D空间的图形对象，如多边形和圆。控制线宽、颜色和锯齿设置等
    9、savefig : 可以对保存的图形进行单独设置。例如，设置渲染的文件背景为白色
    10、text：设置字体颜色、文本解析（纯文本或latex标记）等。
    11、verbose : 设置matplotlib 在执行期间信息输出，如silent、helpful、debug、和debug-annoying
    12、xticks 和 yticks ：为 x、y 轴的刻度和次刻度设置颜色、大小、方向、以及标签大小
"""
m = mpl.get_configdir
