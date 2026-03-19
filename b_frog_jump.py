#!/usr/bin/env python3

# https://atcoder.jp/contests/dp/tasks/dp_b


def solve():
    n, k = list(map(int, input().split()))
    height = list(map(int, input().split()))
    cost = [float("inf")] * n

    def jump(i):
        if i == 0:
            return 0
        if cost[i] != float("inf"):
            return cost[i]

        for j in range(max(0, i - k), i):
            cost[i] = min(cost[i], jump(j) + abs(height[i] - height[j]))
        return cost[i]

    # print(jump(n - 1))

    cost[0] = 0  # base case
    for i in range(1, n):
        for j in range(max(0, i - k), i):
            cost[i] = min(cost[i], cost[j] + abs(height[i] - height[j]))
    print(cost[n - 1])


solve()
