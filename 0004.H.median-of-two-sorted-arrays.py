# 4. 寻找两个正序数组的中位数
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left_1, right_1 = 0, len(nums1) - 1
        left_2, right_2 = 0, len(nums2) - 1
        left_value, right_value = 0, 0
        while True:
            # move left pointer
            if left_1 <= right_1 and left_2 <= right_2:
                if nums1[left_1] <= nums2[left_2]:
                    left_value = nums1[left_1]
                    left_1 += 1
                else:
                    left_value = nums2[left_2]
                    left_2 += 1
            elif left_1 <= right_1 and left_2 > right_2:
                left_value = nums1[left_1]
                left_1 += 1
            elif left_1 > right_1 and left_2 <= right_2:
                left_value = nums2[left_2]
                left_2 += 1
            elif left_1 > right_1 and left_2 > right_2:
                return (left_value + right_value) / 2

            # move right pointer
            if left_1 <= right_1 and left_2 <= right_2:
                if nums1[right_1] >= nums2[right_2]:
                    right_value = nums1[right_1]
                    right_1 -= 1
                else:
                    right_value = nums2[right_2]
                    right_2 -= 1
            elif left_1 <= right_1 and left_2 > right_2:
                right_value = nums1[right_1]
                right_1 -= 1
            elif left_1 > right_1 and left_2 <= right_2:
                right_value = nums2[right_2]
                right_2 -= 1
            elif left_1 > right_1 and left_2 > right_2:
                return left_value


testcase = [
    ([3], [-2, -1]),  # -1
    ([1, 3], [2, 7]),  # 2.5
    ([1, 3], [2]),  # 2
    ([1, 2], [3, 4]),  # 2.5
    ([0, 0], [0, 0]),  # 0
    ([], [1]),  # 1
    ([2], []),  # 2
]

if __name__ == '__main__':
    obj = Solution()
    for nums1, nums2 in testcase:
        print(obj.findMedianSortedArrays(nums1, nums2))
