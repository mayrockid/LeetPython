import collections
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def howManyOnes(num: int) -> int:
            cnt = 0
            while num > 0:
                cnt += num % 2
                num = num // 2
            return cnt

        d = collections.defaultdict(list)

        for i in arr:
            d[howManyOnes(i)].append(i)

        res = []
        for cnt in sorted(d):
            l = d[cnt]
            l.sort()
            res += l

        return res


testcase = [
    [0,1,2,3,4,5,6,7,8],
    [ 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 ],
    [ 10000, 10000 ],
    [ 2, 3, 5, 7, 11, 13, 17, 19 ],
    [ 10, 100, 1000, 10000 ],
]

if __name__ == '__main__':
    o = Solution()
    for arr in testcase:
        print(o.sortByBits(arr))