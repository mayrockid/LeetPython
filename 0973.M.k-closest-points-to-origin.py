# 973. 最接近原点的 K 个点
# https://leetcode-cn.com/problems/k-closest-points-to-origin/

from typing import List
import collections
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        heap = []
        for point in points:
            dis = point[0]**2 + point[1]**2

            heapq.heappush(heap, (-dis, point))
            if len(heap) > K:
                heapq.heappop(heap)

        res = []

        for item in heap:
            res.append(item[1])
        return res


# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         len = collections.defaultdict(list)
#         for p in points:
#             len[p[0]**2 + p[1]**2].append(p)
#         res = []
#         for l in sorted(len):
#             res += len[l]
#         return res[:K]

testcase = [
    [[[ 1, 3 ], [-2, 2]], 1, [[-2, 2]]],
    [[[ 3, 3 ], [ 5, -1 ], [-2, 4]], 2, [[ 3, 3 ], [-2, 4]]],
]

if __name__ == '__main__':
    o = Solution()
    total, cnt = 0, 0
    for points, K, except_ in testcase:
        print(f'points = {points}')
        print(f'K = {K}')
        print(f'Except = {except_}')
        actual = o.kClosest(points, K)
        print(f'Actual = {actual}')
        print(f'Result = {except_ == actual}\n')
        total += 1
        cnt += 1 if except_ == actual else 0

    print(f'Total = {total}, correct = {cnt}, {cnt/total*100:.2f}%.')