#!/usr/bin/env python3


# https://atcoder.jp/contests/dp/tasks/dp_g

from collections import deque


def solve():
    N, M = map(int, input().split())
    G = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)

    # visited = set()
    stack = []

    # def dfs(v):
    #     visited.add(v)
    #     for neighbor in G[v]:
    #         if neighbor not in visited:
    #             dfs(neighbor)
    #     stack.append(v)

    # for v in G:
    #     if v not in visited:
    #         dfs(v)

    indegree = [0] * (N + 1)
    queue = deque()

    for v in range(1, N + 1):
        for u in G[v]:
            indegree[u] += 1

    for v in range(1, N + 1):
        if indegree[v] == 0:
            queue.append(v)

    while queue:
        v = queue.popleft()
        stack.append(v)
        for u in G[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                queue.append(u)

    dist = {v: 0 for v in G}

    stack = stack[::-1]

    while stack:
        u = stack.pop()
        for v in G[u]:
            if dist[v] < dist[u] + 1:
                dist[v] = dist[u] + 1
    max_dist = max(dist.values())
    print(max_dist)


solve()
