#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> data_play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/9 13:40
@Desc    :
================================================="""
import random


def sort_list(aim_list):
    des_list = []
    for item in aim_list:
        if item != 0:
            des_list.append(item)
    print(des_list)


def main():
    data_all = [0, 2, 4, 8, 16, 32, 64]
    a = random.randint(0, 6)
    b = random.randint(0, 6)
    c = random.randint(0, 6)
    d = random.randint(0, 6)
    row_list = [data_all[a], data_all[b], data_all[c], data_all[d]]
    print(row_list)
    sort_list(row_list)


if __name__ == '__main__':
    main()
