# https://leetcode.com/problems/longest-increasing-subsequence/
from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = [1]*len(nums)
        for i in range(len(nums)):
            max_sub = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_sub = max(max_sub,lis[j])
            lis[i] = max_sub + 1
        return max(lis)

    def lengthOfLIS_BinarySearch(self, nums: list[int]) -> int:
        arr = [nums.pop(0)]                  # <-- 1) initial step
        for n in nums:                       # <-- 2) iterate through nums
            if n > arr[-1]:                  # <--    2a)
                arr.append(n)
            else:                            # <--    2b)
                arr[bisect_left(arr, n)] = n 
        return len(arr) 