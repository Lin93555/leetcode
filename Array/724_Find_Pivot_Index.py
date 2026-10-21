# LeetCode 724. Find Pivot Index（寻找数组的中心下标）
# 难度：Easy
#
# 题意：找一个下标 i，使它左边所有数之和等于右边所有数之和；
#       有多个返回最左边的，没有返回 -1。
#
# 思路：先求总和 total。从左往右扫，维护左边之和 left_sum，
#       右边之和 = total - left_sum - nums[i]，两者相等就找到了。
# 复杂度：时间 O(n)，空间 O(1)

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            if left_sum == total - left_sum - x:
                return i
            left_sum += x
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert s.pivotIndex([1, 2, 3]) == -1
    assert s.pivotIndex([2, 1, -1]) == 0
    print("all tests passed")
