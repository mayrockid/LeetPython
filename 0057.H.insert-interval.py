# 57. 插入区间
# https://leetcode-cn.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        left, right = None, None
        for index, interval in enumerate(intervals):
            if left is None:
                if interval[1] < newInterval[0]:
                    continue
                if newInterval[0] <= interval[1]:
                    left = min(interval[0], newInterval[0])
                    left_idx = index
            if right is None:
                if newInterval[1] < interval[0]:
                    right = newInterval[1]
                    right_idx = index
            if interval[0] <= newInterval[1]:
                right = max(interval[1], newInterval[1])
                right_idx = index + 1
            if left is None and right is None:
                if newInterval[1] < interval[0]:
                    return [newInterval] + intervals
                if interval[0] <= newInterval[0] and newInterval[1] <= interval[1]:
                    return intervals

        if left is None and right is None:
            return intervals + [newInterval]
        elif left is not None and right is None:
            return intervals[:left_idx] + [[ left, max(intervals[-1][1], newInterval[1]) ]]
        elif left is None and right is not None:
            return [[min(intervals[0][0], newInterval[0]), right]] + intervals[right_idx:]
        elif left is not None and right is not None:
            return intervals[:left_idx] + [[ left, right ]] + intervals[right_idx:]


testcase = [
    [[[ 3, 5 ], [ 12, 15 ]], [ 6, 7 ], [[ 3, 5 ], [ 6, 7 ], [ 12, 15 ]]],
    [[[ 0, 7 ], [ 9, 11 ]], [ 4, 13 ], [[ 0, 13 ]]],
    [[[ 0, 5 ], [ 8, 9 ]], [ 3, 4 ], [[ 0, 5 ], [ 8, 9 ]]],
    [[[ 1, 2 ], [ 3, 5 ], [ 6, 7 ], [ 8, 10 ], [ 12, 16 ]], [ 4, 8 ], [[ 1, 2 ], [ 3, 10 ], [ 12, 16 ]]],
    [[[ 1, 2 ], [ 3, 5 ], [ 6, 7 ], [ 8, 10 ], [ 12, 16 ]], [ 4, 12 ], [[ 1, 2 ], [ 3, 16 ]]],
    [[[ 1, 5 ]], [ 0, 6 ], [[ 0, 6 ]]],
    [[[ 1, 5 ], [ 6, 9 ]], [ 0, 3 ], [[ 0, 5 ], [ 6, 9 ]]],
    [[[ 1, 5 ]], [ 0, 3 ], [[ 0, 5 ]]],
    [[[ 1, 5 ], [ 6, 9 ]], [ 7, 11 ], [[ 1, 5 ], [ 6, 11 ]]],
    [[[ 1, 5 ]], [ 2, 7 ], [[ 1, 7 ]]],
    [[[ 3, 5 ], [ 6, 8 ]], [ 1, 2 ], [[ 1, 2 ], [ 3, 5 ], [ 6, 8 ]]],
    [[[ 3, 5 ], [ 6, 8 ]], [ 10, 12 ], [[ 3, 5 ], [ 6, 8 ], [ 10, 12 ]]],
    [[[ 1, 3 ], [ 6, 9 ]], [ 2, 5 ], [[ 1, 5 ], [ 6, 9 ]]],
    [[], [ 5, 7 ], [[ 5, 7 ]]],
    [[[ 5, 7 ]], [], [[ 5, 7 ]]],
]

if __name__ == '__main__':
    o = Solution()
    cnt, total = 0, 0
    for intervals, newInterval, except_ in testcase:
        print(f'intervals = {intervals}')
        print(f'newInterval = {newInterval}')
        print(f'Except = {except_}')
        actual = o.insert(intervals, newInterval)
        print(f'Actual = {actual}')
        print(f'Result = {except_ == actual}\n')
        total += 1
        cnt += 1 if except_ == actual else 0

    print(f'Total = {total}, correct = {cnt}, {cnt/total*100:.2f}%.')
