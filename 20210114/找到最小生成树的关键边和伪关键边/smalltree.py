#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> smalltree.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/21 16:31
@Desc    :
================================================="""


def findCriticalAndPseudoCriticalEdges(n, edges):
    parent = list(range(n))

    def find(index):
        if index != parent[index]:
            parent[index] = find(parent[index])
        return parent[index]

    def union(index1, index2):
        parent[index2] = index1

    # 这里由小到大排序 就是 Kruskal 的思想
    # 在原有的edge中添加位置索引，方便排序后能得到在原edges中的位置
    sorted_edges = [[index] + i for index, i in enumerate(edges)]
    # 根据 weight 对边进行排序
    sorted_edges = sorted(sorted_edges, key=lambda x: x[-1])

    # 计算最小生成树的权值和 total
    total = 0
    for index, (_, x, y, w) in enumerate(sorted_edges):
        rx, ry = find(x), find(y)
        if rx != ry:
            union(rx, ry)
            total += w
    print(total)

    # 接下来 进行 最小生成树的构造 分为两种情况：
    # 1.先连接当前边，得到所有连通边的权值和 total1
    # 若 total与total1 相等，则代表 该边为有效边， 否则为无效边直接跳过
    # 2.去掉当前边，得到所有连通边的权值和 total2
    # 若 total1不等于total2，则代表该边为 关键边， 否则为 防关键边

    key_edge = []  # 关键边列表
    no_key_edge = []  # 非关键边列表
    for i, edge in enumerate(sorted_edges):
        (_, cx, cy, cw) = edge
        # 去掉当前边, 形成新的边列表
        tmp_edges = sorted_edges[:i] + sorted_edges[i + 1:]

        # 1.先连接当前边，得到连通边的权值和 total1
        total1 = cw
        parent = list(range(n))
        union(cx, cy)
        for index, (_, x, y, w) in enumerate(tmp_edges):
            rx, ry = find(x), find(y)
            if rx != ry:
                union(rx, ry)
                total1 += w

        # 若 total与total1 相等，则代表 该边为有效边， 否则为无效边直接跳过
        if total != total1: continue

        # 2.去掉当前边，得到连通边的权值和 total2
        total2 = 0
        parent = list(range(n))
        for index, (_, x, y, w) in enumerate(tmp_edges):
            rx, ry = find(x), find(y)
            if rx != ry:
                union(rx, ry)
                total2 += w

        # 若 total1不等于total2，则代表该边为 关键边， 否则为 伪关键边

        if total1 != total2:
            key_edge.append(edge[0])
        else:
            no_key_edge.append(edge[0])

    return [key_edge, no_key_edge]


def main():
    n = 5
    edges = [[1, 2, 1], [2, 3, 2], [0, 1, 1], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
    result = findCriticalAndPseudoCriticalEdges(n, edges)
    print(result)


if __name__ == '__main__':
    main()
