# 327. 区间和的个数
# https://leetcode-cn.com/problems/count-of-range-sum/

from typing import List
import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res
