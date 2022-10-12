# https://leetcode.com/problems/house-robber/
## DP Approacj, only two previous data needed, max_till previous step and previous step.

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_till = 0
        prev_step = 0
        current_step = 0
        for num in nums:
            current_step = max(max_till+num, prev_step)
            max_till = prev_step
            prev_step = current_step
        return current_step