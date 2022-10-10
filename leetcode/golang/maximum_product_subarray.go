package leetcode

import "math"

// maxProduct https://leetcode.com/problems/maximum-product-subarray/.
// Greedy approach. scanning twice
func maxProduct(nums []int) int {
	max_prod := -math.MaxInt32
	max_prod_window := 1
	// left := 0
	right := 0
	for right < len(nums) {
		max_prod_window *= nums[right]
		if max_prod_window > max_prod {
			max_prod = max_prod_window
		}
		if max_prod_window == 0 {
			// left = right +1
			max_prod_window = 1
		}
		right += 1
	}
	right = len(nums) - 1
	max_prod_window = 1
	for right >= 0 {
		max_prod_window *= nums[right]
		if max_prod_window > max_prod {
			max_prod = max_prod_window
		}
		if max_prod_window == 0 {
			// left = right +1
			max_prod_window = 1
		}
		right -= 1
	}

	return max_prod

}
