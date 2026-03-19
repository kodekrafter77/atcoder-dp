#!/usr/bin/env python3

# https://atcoder.jp/contests/dp/tasks/dp_d


def solve():
    N, W = tuple(map(int, input().split()))
    weights = []
    values = []
    for _ in range(N):
        wt, v = tuple(map(int, input().split()))
        weights.append(wt)
        values.append(v)

    knapsack_value = [[0] * (W + 1) for _ in range(N + 1)]

    def pickup(item, weight):
        if item == 0 or weight == 0:
            return 0
        if knapsack_value[item][weight] != -1:
            return knapsack_value[item][weight]

        # skip this item
        leave_behind = pickup(item - 1, weight)

        # pick this item (only if it fits)
        pick = 0
        if weights[item - 1] <= weight:
            pick = pickup(item - 1, weight - weights[item - 1]) + values[item - 1]

        knapsack_value[item][weight] = max(pick, leave_behind)
        return knapsack_value[item][weight]

    # print(pickup(N, W))

    for i in range(1, N + 1):
        for w in range(W + 1):
            knapsack_value[i][w] = knapsack_value[i - 1][w]
            if w >= weights[i - 1]:
                knapsack_value[i][w] = max(
                    knapsack_value[i][w],
                    values[i - 1] + knapsack_value[i - 1][w - weights[i - 1]],
                )

    print(knapsack_value[N][W])


solve()
