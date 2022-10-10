package leetcode

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// maxArea https://leetcode.com/problems/container-with-most-water/.
func maxArea(height []int) int {
	left := 0
	right := len(height) - 1
	max_capacity := 0
	for left < right {
		capacity := min(height[left], height[right]) * (right - left)
		if capacity > max_capacity {
			max_capacity = capacity
		}
		if height[left] < height[right] {
			left += 1
		} else {
			right -= 1
		}
	}
	return max_capacity
}
