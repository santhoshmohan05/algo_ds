# https://leetcode.com/problems/counting-bits
# Reference: https://leetcode.com/problems/counting-bits/discuss/656849/Python-Simple-Solution-with-Clear-Explanation
class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]*(n+1)
        if n == 0:
            return counter
        counter[1] = 1
        for i in range(2,n+1):
            counter[i] = counter[i>>1] + (i%2)
        return counter
        
    def countBitsMy(self, n: int) -> List[int]:
        output = [0]*(n+1)
        if n == 0:
            return output
        output[1] = 1
        if n==1:
            return output
        output[2] = 1
        last_2 = 2
        for i in range(3,n+1):
            output[i] = output[i%last_2] +1
            if i/last_2 == 2:
                last_2 = i
        return output
    
        
        