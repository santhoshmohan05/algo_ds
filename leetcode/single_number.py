# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        for i in nums:
            one= one ^ i
        return one
