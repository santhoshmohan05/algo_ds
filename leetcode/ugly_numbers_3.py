# https://leetcode.com/problems/ugly-number-iii

from math import gcd
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 0
        right = n*min(a,b,c)
        def lcm(x,y):
            return x*y//gcd(x,y)
        ab = lcm(a,b)
        bc = lcm(b,c)
        ca = lcm(c,a)
        abc = lcm(ab,c)
        def get_multiples(number):
            nonlocal a,b,c,ab,bc,ca,abc
            return number//a + number//b + number//c - number//ab - number//bc - number//ca + number//abc
    
        while left < right:
            mid = left + ((right - left)//2)
            factors = get_multiples(mid)
            if factors >= n:
                right = mid
            else:
                left = mid+1
        return left
            
        