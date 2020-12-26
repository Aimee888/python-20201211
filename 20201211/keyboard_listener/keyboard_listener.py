#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20201211 -> keyboard_listener.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/12/11 14:52
@Desc    :参考链接：https://www.jb51.net/article/196077.htm
================================================="""
import sys, os
from pynput.keyboard import Controller, Key, Listener


# 监听按压
def on_press(key):
    try:
        print("正在按压:", format(key.char))
    except AttributeError:
        print("正在按压:", format(key))


# 监听释放
def on_release(key):
    print("已经释放:", format(key))

    if key == Key.esc:
        # 停止监听
        return False


# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    # 实例化键盘
    kb = Controller()

    # 开始监听,按esc退出监听
    start_listen()

