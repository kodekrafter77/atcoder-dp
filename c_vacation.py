#!/usr/bin/env python3

# https://atcoder.jp/contests/dp/tasks/dp_c


def solve():
    N = int(input())
    activities = []
    for _ in range(N):
        day_activity = list(map(int, input().split()))
        activities.append(day_activity)

    """ Recurrence relation:
        best_happiness(day, activity) = activities[day][activity] + max(best_happiness(day - 1, other_activity)) where other_activity != activity
    """

    total_points = [[-1 for _ in range(3)] for _ in range(N)]

    # top-down memoized solution
    def best_happiness(day, activity):
        if day == 0:
            return activities[day][activity]

        if total_points[day][activity] != -1:
            return total_points[day][activity]

        happiness = activities[day][activity]
        happiness += max(best_happiness(day - 1, k) for k in range(3) if k != activity)
        total_points[day][activity] = happiness
        return happiness

    # Uncomment below 4 lines to try top-down recursive memoized solution
    # res = max(
    #     best_happiness(N - 1, 0), best_happiness(N - 1, 1), best_happiness(N - 1, 2)
    # )
    # print(res)

    # At this point the above top-down memoized solution gives runtime error when submitted to atcoder.jp.
    # Best possible solution is bottom-up iterative DP

    total_points[0][0] = activities[0][0]
    total_points[0][1] = activities[0][1]
    total_points[0][2] = activities[0][2]

    for day in range(1, N):
        for activity in range(3):
            total_points[day][activity] = (
                max(total_points[day - 1][k] for k in range(3) if k != activity)
                + activities[day][activity]
            )
    print(max(total_points[N - 1]))


solve()
