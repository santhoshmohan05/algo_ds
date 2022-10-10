package leetcode

import "math"

// maxSubArray https://leetcode.com/problems/maximum-subarray/.
func maxSubArray(nums []int) int {
	max_sum := -math.MaxInt32
	max_sum_until := 0
	for _, c := range nums {
		max_sum_until = max_sum_until + c
		if max_sum_until > max_sum {
			max_sum = max_sum_until
		}
		if max_sum_until < 0 {
			max_sum_until = 0
		}

	}
	return max_sum

}
