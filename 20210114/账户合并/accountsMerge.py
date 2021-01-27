#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : python-20201211 -> accountsMerge.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2021/1/19 8:49
@Desc    :深度遍历方法 -- LeetCode
================================================="""
import collections


class Solution:
    def accountsMerge(self, accounts):
        # 构建无向图，每个邮箱为一个节点，同一个账户的邮箱全部相连
        # 有多少连通分量，就有多少独立的账户
        # 该字典，键为一个邮箱，值为与其相连的所有邮箱
        graph = collections.defaultdict(list)
        for account in accounts:
            master = account[1]
            for email in list(set(account[2:])):
                graph[master].append(email)
                graph[email].append(master)

        res = []  # 最终的输出结果
        visited = set()  # 标记集合
        print(graph)

        for account in accounts:
            emails = []  # 存储该账户的所有邮箱
            # 深度优先遍历
            self.dfs(account[1], graph, visited, emails)
            if emails:
                res.append([account[0]] + sorted(emails))
        return res

    # 深度优先遍历
    def dfs(self, email, graph, visited, emails):
        # 访问过，不在添加直接结束
        if email in visited:
            return
        visited.add(email)  # 标记访问
        emails.append(email)  # 添加
        for neighbor in graph[email]:
            self.dfs(neighbor, graph, visited, emails)


if __name__ == '__main__':
    # input = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
    #          ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
    #          ["David", "David1@m.co", "David2@m.co"]]
    input = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
             ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
    print(input)
    output = Solution().accountsMerge(input)
    # print(output)
