# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime
def xTimePlt(x, y):
    fig = plt.figure(figsize=(24, 12))
    plt.plot(x, y, linestyle='-', marker='*', c='r', alpha=0.5)
    ax = plt.gca()
    date_format = mpl.dates.DateFormatter('%Y-%m-%d')  # 设定显示的格式形式
    ax.xaxis.set_major_formatter(date_format)  # 设定x轴主要格式
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(7))  # 设定坐标轴的显示的刻度间隔
    fig.autofmt_xdate()  # 防止x轴上的数据重叠，自动调整。
    plt.grid()


start=datetime.datetime(2018, 1, 1)
stop=datetime.datetime(2018,12,31)
delta=datetime.timedelta(30)#设定日期的间隔
dates_X=mpl.dates.drange(start,stop,delta)
dates_Y=np.random.randint(0,2,len(dates_X))

xTimePlt(dates_X, dates_Y)

plt.show()