# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for num in nums:
            # print(one,two,num)
            two = two ^ (one & num)
            one = one ^ num
            
            common_bits_mask = ~(two & one)
            one = one & common_bits_mask
            two = two & common_bits_mask
        # print(one,two,num)
        return one
            