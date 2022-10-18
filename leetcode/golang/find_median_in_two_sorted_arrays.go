package leetcode

// findMedianSortedArrays - https://leetcode.com/problems/median-of-two-sorted-arrays.
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	n := len(nums1) + len(nums2)
	res := 0
	if n%2 == 1 {
		res = findK(nums1, nums2, n/2)
		return float64(res)
	} else {
		res = findK(nums1, nums2, n/2) + findK(nums1, nums2, (n/2)-1)
		return float64(res) / 2.0
	}

}

func findK(a []int, b []int, k int) int {
	// fmt.Println(a,b,k)
	ia := len(a) / 2
	ib := len(b) / 2
	if len(a) == 0 {
		return b[k]
	}
	if len(b) == 0 {
		return a[k]
	}
	if ia+ib < k {
		if a[ia] < b[ib] {
			return findK(a[ia+1:], b, k-ia-1)
		} else {
			return findK(a, b[ib+1:], k-ib-1)
		}
	} else {
		if a[ia] < b[ib] {
			return findK(a, b[:ib], k)
		} else {
			return findK(a[:ia], b, k)
		}
	}
}
