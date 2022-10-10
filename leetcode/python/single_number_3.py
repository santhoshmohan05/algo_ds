# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor = xor ^ i
        rmsb = xor & - xor
        ans = [0,0]
        for  i in nums:
            if i & rmsb == 0:
                ans[0] = ans[0] ^ i
            else:
                ans[1] = ans[1] ^ i
        return ans