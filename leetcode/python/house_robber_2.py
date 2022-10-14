# https://leetcode.com/problems/house-robber-ii/
## DP Approacj, only two previous data needed, max_till previous step and previous step.

class Solution:
    def robSimple(self, nums: List[int]) -> int:
        max_till = 0
        prev_step = 0
        current_step = 0
        for num in nums:
            current_step = max(max_till+num, prev_step)
            max_till = prev_step
            prev_step = current_step
        return current_step
    
    def robCircle(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self.robSimple(nums[1:]), self.robSimple(nums[:-1]))