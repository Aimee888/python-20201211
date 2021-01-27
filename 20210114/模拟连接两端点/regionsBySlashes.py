#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> regionsBySlashes.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/25 14:16
@Desc    :
================================================="""


# 并查集
class unionfind:
    def __init__(self, n):
        self.parent = list(range(n * n + 2 * n + 2))
        self.area = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.parent[xroot] = yroot

    def isClosed(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            self.area += 1
            return True
        else:
            return False


def regionsBySlashes(grid):
    n = len(grid)
    uf = unionfind(n)

    # 连接边缘
    node = n * n + 2 * n + 1
    for i in range(n + 1):
        uf.union(node, i)  # 连接上边缘
        uf.union(node, n * n + n + i)  # 连接下边缘
        uf.union(node, i * (n + 1))  # 连接左边缘
        uf.union(node, i * (n + 1) + n)  # 连接右边缘

    # 连接斜杠
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '/':
                node1 = (n + 1) * (i + 1) + j
                node2 = (n + 1) * i + (j + 1)
                if not uf.isClosed(node1, node2):
                    uf.union(node1, node2)
            elif grid[i][j] == '\\':
                node1 = (n + 1) * i + j
                node2 = (n + 1) * (i + 1) + (j + 1)
                if not uf.isClosed(node1, node2):
                    uf.union(node1, node2)

    return uf.area


if __name__ == '__main__':
    data = [" /", "/ "]
    result = regionsBySlashes(data)
    print(result)
