# https://leetcode.com/problems/coin-change/
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [-1]*(amount+1)
        table[0] = 0

        for i in range(1,amount+1):
            min_coins = amount+1
            for j in coins:
                if (i - j) >=0 and table[i-j] != -1:
                    min_coins = min(min_coins,table[i-j])
            if min_coins != amount+1:
                table[i] = min_coins + 1

        return table[-1]
