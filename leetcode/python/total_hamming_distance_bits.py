# https://leetcode.com/problems/total-hamming-distance
"""
For each bit, count how many numbers have 0 or 1 on that bit; the total difference on that bit is zero * ones
"""
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        for i in range(32):
            ones = sum([(k>>i & 1) for k in nums])
            total += ones * (len(nums) - ones)
        return total
            
            
        