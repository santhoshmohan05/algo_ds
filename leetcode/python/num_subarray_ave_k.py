# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sliding_sum = 0
        left = 0
        right = 0
        output = 0
        while right < len(arr):
            sliding_sum += arr[right]
            right += 1
            if (right - left) < k:
                continue
            elif (right - left) == k:
                if (sliding_sum / k) >= threshold:
                    output += 1
                sliding_sum -= arr[left]
                left += 1
        return output
                    
                    