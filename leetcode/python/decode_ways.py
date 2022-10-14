# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        if len(s) <= 1:
            return len(s)
        dp[0] = 1
        for i in range(1,len(s)+1):
            if s[i-1] != 0:
                dp[i] = dp[i-1]
            if i >= 2:
                number = int(s[i-2:i])
                if 10 <= number <= 26:
                    dp[i] += dp[i-2]
        return dp[len(s)]
