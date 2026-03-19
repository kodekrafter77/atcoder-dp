#!/usr/bin/env python3

# https://atcoder.jp/contests/dp/tasks/dp_a


def solve():
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    t = [float("inf")] * n

    # Recursive top-down memoized version
    def jump(i):
        if i == n - 1:
            return 0

        if t[i] != float("inf"):
            return t[i]

        res = float("inf")

        if i + 1 < n:
            res = min(res, abs(nums[i] - nums[i + 1]) + jump(i + 1))

        if i + 2 < n:
            res = min(res, abs(nums[i] - nums[i + 2]) + jump(i + 2))

        t[i] = res
        return res

    # print(jump(0))

    t[0] = 0  # base case: already at stone 0

    for i in range(1, n):
        # came from i-1 (1-step jump)
        t[i] = t[i - 1] + abs(nums[i] - nums[i - 1])
        # came from i-2 (2-step jump)
        if i >= 2:
            t[i] = min(t[i], t[i - 2] + abs(nums[i] - nums[i - 2]))

    print(t[n - 1])


if __name__ == "__main__":
    solve()
