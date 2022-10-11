# https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        answer = 0
        i = 0
        while i<32:
            answer = (answer << 1) + (n&1)
            n = n >> 1
            i+=1
        return answer