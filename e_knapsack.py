#!/usr/bin/env python3

# https://atcoder.jp/contests/dp/tasks/dp_e


def solve():
    N, W = map(int, input().split())
    weights = []
    values = []
    for _ in range(N):
        wt, v = map(int, input().split())
        weights.append(wt)
        values.append(v)

    V = sum(values)

    knapsack_value = [[float("inf")] * (V + 1) for _ in range(N + 1)]

    def pickup(item, value):
        if value == 0:
            return 0
        if item == 0:
            return float("inf")

        if knapsack_value[item][value] is not None:
            return knapsack_value[item][value]

        # skip this item
        leave_behind = pickup(item - 1, value)

        # pick this item (only if value is achievable)
        pick = float("inf")
        if values[item - 1] <= value:
            pick = pickup(item - 1, value - values[item - 1]) + weights[item - 1]

        knapsack_value[item][value] = min(pick, leave_behind)
        return knapsack_value[item][value]

    # find largest value achievable within weight W
    # for v in range(V, -1, -1):
    #     if pickup(N, v) <= W:
    #         print(v)
    #         break

    knapsack_value[0][0] = 0

    for i in range(1, N + 1):
        for v in range(V + 1):
            # skip item i
            knapsack_value[i][v] = knapsack_value[i - 1][v]

            # pick item i (if value is achievable)
            if (
                v >= values[i - 1]
                and knapsack_value[i - 1][v - values[i - 1]] + weights[i - 1]
                < knapsack_value[i][v]
            ):
                knapsack_value[i][v] = (
                    knapsack_value[i - 1][v - values[i - 1]] + weights[i - 1]
                )

    # find largest value achievable within weight W
    for v in range(V, -1, -1):
        if knapsack_value[N][v] <= W:
            print(v)
            break


solve()
