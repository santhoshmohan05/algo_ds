package leetcode

// maxProfit https://leetcode.com/problems/best-time-to-buy-and-sell-stock/.
func maxProfit(prices []int) int {
	profit := 0
	buy := prices[0]

	for i := 1; i < len(prices); i++ {
		if prices[i] < buy {
			buy = prices[i]
		} else if profit < prices[i]-buy {
			profit = prices[i] - buy
		}
	}
	return profit
}
