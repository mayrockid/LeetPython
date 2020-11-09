# 122. 买卖股票的最佳时机 II
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, sum, gotLeft = 0, 0, False
        for i in range(len(prices) - 1):
            if gotLeft:
                if prices[i + 1] < prices[i]:
                    sum += prices[i] - left
                    gotLeft = False
            else:
                if prices[i + 1] >= prices[i]:
                    left = prices[i]
                    gotLeft = True

        if gotLeft:
            return sum + prices[-1] - left
        else:
            return sum


testcase = [
    [ 7, 1, 5, 3, 6, 4 ],
    [ 1, 2, 3, 4, 5 ],
    [ 7, 6, 4, 3, 1 ],
]

if __name__ == '__main__':
    o = Solution()
    for prices in testcase:
        print(o.maxProfit(prices))