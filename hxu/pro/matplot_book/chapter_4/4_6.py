# -*-coding:utf-8 -*-
"""
格式化定制网格
可以通过主刻度或者次刻度，或者同时通过两个刻度来操作网格。
因此，函数参数which可以是“major”、“minor”、或者“both”
与此类似，可以通过参数axis分别控制水平刻度和垂直刻度，参数值可以是“x”、“y”或者“both”
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from matplotlib.cbook import get_sample_data


def get_demo_image():
    # f = get_sample_data('axes_grid/bivariate_normal.npy', asfileobj=False)

    f = get_sample_data('camera_wiener.npy', asfileobj=False)
    # z is a numpy array of 15 x 15
    z = np.load(f)
    return z, (-3, 4, -4, 3)


def get_grid(fig=None, layout=None, nrows_ncols=None):
    assert fig is not None
    assert layout is not None
    assert nrows_ncols is not None

    grid = ImageGrid(fig, layout, nrows_ncols=nrows_ncols, axes_pad=0.05, add_all=True, label_mode='L')
    return grid


def load_images_to_grid(grid, z, *images):
    min, max = z.min(), z.max()
    for i, image in enumerate(images):
        axes = grid[i]
        axes.imshow(image, origin='lower', vmin=min, vmax=max, interpolation='nearest')


if __name__ == '__main__':
    fig = plt.figure(1, (8, 6))
    grid = get_grid(fig, 111, (1, 3))
    z, extent = get_demo_image()

    # Slice image
    image1 = z
    image2 = z[:, :10]
    image3 = z[:, 10:]

    load_images_to_grid(grid, z, image1, image2, image3)
    plt.draw()
    plt.show()