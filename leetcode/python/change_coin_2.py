# https://leetcode.com/problems/coin-change-ii/

class Solution:    
    def change(self, amount: int, coins: List[int]) -> int:
        change = [0]*(amount+1)
        change[0] = 1
        for i in range(len(coins)):
            for j in range(amount+1):
                change[j] += change[j - coins[i]] if j - coins[i] >= 0 else 0
        return change[-1]
