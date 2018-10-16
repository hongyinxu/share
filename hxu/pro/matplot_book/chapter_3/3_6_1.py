# -*- coding:utf-8 -*-
"""
matplotlib.dates.date2num(), matplot.dates.num2date() 和 matplotlib.dates.drange()实现对日期进行不同形式的转换
"""
import matplotlib.pyplot as plt
from matplotlib import dates as da
import datetime
import numpy as np

fig = plt.figure()

# get current axis
ax = plt.gca()

# set some daterange
start = datetime.datetime(2013, 1, 1, 0, 0, 0)
stop = datetime.datetime(2013, 1, 10, 0, 0, 0)
delta = datetime.timedelta(hours=1)

# convert dates for matplotlib
dates = da.drange(start, stop, delta)

values = np.random.rand(len(dates))

# ax1 = plt.gca()

# create plot with dates
ax.plot_date(dates, values, linestyle='-', marker='')

# specify formater
date_format = da.DateFormatter('%Y-%m-%d %H:%M:%s')

# apply formatter
ax.xaxis.set_major_formatter(date_format)

# autoformat date labels
# rotates labels by 30 30 degrees by default
# use rotate para to specify different rotation degree
# use bottom param to give more room to date labels
fig.autofmt_xdate()
plt.show()