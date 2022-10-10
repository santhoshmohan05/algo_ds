package leetcode

// search https://leetcode.com/problems/search-in-rotated-sorted-array.
func search(nums []int, target int) int {
	left := 0
	right := len(nums) - 1
	for left < right {
		mid := left + ((right - left) / 2)
		if nums[mid] == target {
			return mid
		}
		if nums[mid] >= nums[left] {
			if nums[left] <= target && target <= nums[mid] {
				right = mid
			} else {
				left = mid + 1
			}
		} else if nums[mid] < nums[right] {
			if nums[mid] < target && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid
			}

		}
	}
	if nums[left] == target {
		return left
	}
	return -1
}
