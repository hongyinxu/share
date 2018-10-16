#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
"""
from datetime import datetime, timedelta, timezone


"""返回当前日期和时间"""
now = datetime.now()        # 2018-10-12 22:00:23.525503

# try:
#     print(now)
# except ValueError as e:
#     print("ValueError", e)
# finally
#     print('task end')
"""返回utc时间"""
now1 = datetime.utcnow()        # 2018-10-12 14:00:23.526503

"""用指定日期时间创建datetime"""
dt = datetime(2015, 4, 19, 12, 20, 20)  # 2015-04-19 12:20:20

# -----------------------------------------------------
"""
datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），
# 当前时间就是相对于epoch time的秒数，称为timestamp。
# 可以认为： timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00 对应的北京时间是： timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# 可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
# 这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
"""

"""datetime转换为timestamp,注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。"""
a = dt.timestamp()      # 1429417220.0

# ---------------------------------------------------------
"""timestamp转换为datetime
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
# print(datetime.fromtimestamp(a))    # 实际上就是UTC+8:00时区的时间 2015-04-19 12:20:00 UTC+8:00
# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
# print(datetime.utcfromtimestamp(a))     # 直接被转换到UTC标准时区的时间：
"""
local_time = datetime.fromtimestamp(a)       # 2015-04-19 12:20:20
utc_time = datetime.utcfromtimestamp(a)      # 2015-04-19 04:20:20
# -----------------------------------------------------------------------------------
"""str转换为datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
# 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
"""
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')  # 2015-06-01 18:19:59

# -----------------------------------------------------------------------------------------
"""datetime转换为str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
"""
now_str = now.strftime('%a, %b %d, %H:%M')       # Fri, Oct 12, 22:08
now_str_1 = now.strftime('%Y, %m %d, %H:%M:%S')  # 2018, 10 12, 22:09:54
# --------------------------------------------------------------------------------------

"""datetime加减
"""
now = datetime.now()    # now = 2018-10-12 22:12:51.182266
print('type(now) =', type(now))     # type(now) = <class 'datetime.datetime'>

"""对日期进行加减:"""
print('current datetime =', cday)   # current datetime = 2015-06-01 18:19:59
print('current + 10 hours =', cday + timedelta(hours=10))   # current + 10 hours = 2015-06-02 04:19:59
print('current - 1 day =', cday - timedelta(days=1))    # current - 1 day = 2015-05-31 18:19:59
print('current + 2.5 days =', cday + timedelta(days=2, hours=12))   # current + 2.5 days = 2015-06-04 06:19:59
print('current + 2.5 days =', cday + timedelta(days=2.5))   # current + 2.5 days = 2015-06-04 06:19:59

"""把时间从UTC+0时区转换为UTC+8:"""
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)     # UTC+0:00 now = 2018-10-12 14:18:51.677885+00:00
utc_dt = datetime.utcnow()                                    # UTC+0:00 now = 2018-10-12 14:18:51.677885+00:00
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))   # UTC+8:00 now = 2018-10-12 22:18:51.677885+08:00

time = datetime(1998, 11, 17)
time_sta = datetime(1970, 1, 1)
time_map0 = time.timestamp()    # 911232000.0(s) = 10546.666666666666(day)
time_map = time-time_sta        # 10547 days, 0:00:00

timestamp = -1893436000
dt = datetime(1970, 1, 1) + timedelta(microseconds=timestamp)   # 微秒    # 1969-12-31 23:28:26.564000
print(dt)

