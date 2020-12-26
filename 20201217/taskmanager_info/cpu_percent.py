#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20201211 -> cpu_percent.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/12/17 10:48
@Desc    :参考链接：https://blog.csdn.net/zigewb/article/details/80221934
================================================="""
import psutil
import time


# function of Get CPU State;
def getCPUstate():
    # print(psutil.cpu_percent(interval=1, percpu=True))
    print(psutil.cpu_percent(interval=1))
    # print(psutil.cpu_times_percent(1))


while 1:
    time.sleep(1)
    getCPUstate()
