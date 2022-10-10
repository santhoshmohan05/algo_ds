package leetcode

// containsDuplicate https://leetcode.com/problems/contains-duplicate/.
func containsDuplicate(nums []int) bool {
	count := make(map[int]bool)
	for _, c := range nums {
		if _, prs := count[c]; prs == true {
			return true
		}
		count[c] = true
	}
	return false
}
