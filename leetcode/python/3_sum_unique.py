# https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        output = []
        i = 0
        while i < len(nums):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    output.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left +=1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i+=1
        return output
            
                
                