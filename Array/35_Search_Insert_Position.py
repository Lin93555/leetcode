# LeetCode 35. Search Insert Position（搜索插入位置）
# 难度：Easy
#
# 题意：给定一个升序、无重复的数组和目标值 target，
#       找到 target 的下标；不存在就返回它应该插入的位置。
#
# 思路：二分查找。循环结束时 left 就是第一个 >= target 的位置，
#       正好是插入位置。
# 复杂度：时间 O(log n)，空间 O(1)

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    print("all tests passed")
