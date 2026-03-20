#!/usr/bin/env python3


# https://atcoder.jp/contests/dp/tasks/dp_f


def solve():
    s = input()
    t = input()
    matched_sequence = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]

    def lcs(s, t, m, n, matched_sequence):
        if m == 0 or n == 0:
            return 0
        if matched_sequence[m][n] != -1:
            return matched_sequence[m][n]
        if s[m - 1] == t[n - 1]:
            matched_sequence[m][n] = 1 + lcs(s, t, m - 1, n - 1, matched_sequence)
        else:
            matched_sequence[m][n] = max(
                lcs(s, t, m - 1, n, matched_sequence),
                lcs(s, t, m, n - 1, matched_sequence),
            )
        return matched_sequence[m][n]

    # lcs(s, t, len(s), len(t), matched_sequence)

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                matched_sequence[i][j] = 1 + matched_sequence[i - 1][j - 1]
            else:
                matched_sequence[i][j] = max(
                    matched_sequence[i - 1][j], matched_sequence[i][j - 1]
                )

    res = []
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            res.append(s[i - 1])
            i -= 1
            j -= 1
        elif matched_sequence[i - 1][j] >= matched_sequence[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("".join(reversed(res)))


solve()
