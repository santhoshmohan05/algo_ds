# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

## Better Method - https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/discuss/1955208/O(sqrt(total))-Python-0.21-ms-JavaC%2B%2B-0-ms

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        pen_ways = (total // cost1) +1
        for i in range(0,pen_ways):
            pencil_ways = ((total - i*cost1) // cost2) + 1
            ans += pencil_ways
        return ans
            
        