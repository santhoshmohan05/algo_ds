package leetcode

// twoSum https://leetcode.com/problems/two-sum.
func twoSum(nums []int, target int) []int {
	count := make(map[int]int)
	for i, c := range nums {
		value, prs := count[target-c]
		if prs == true {
			return []int{value, i}
		} else {
			count[c] = i
		}
	}
	return make([]int, 2)
}
