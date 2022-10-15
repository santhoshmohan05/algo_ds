# https://leetcode.com/problems/count-vowels-permutation/
### DP - maintain state for each vowel and return sum
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        cache = {}
        cache['a'] = [1]
        cache['e'] = [1]
        cache['i'] = [1]
        cache['o'] = [1]
        cache['u'] = [1]
        mod = 10**9+7
        for i in range(1,n+1):
            cache['a'].append((cache['e'][i-1]+cache['u'][i-1]+cache['i'][i-1])%mod)
            cache['e'].append((cache['a'][i-1]+cache['i'][i-1])%mod)
            cache['i'].append((cache['e'][i-1]+cache['o'][i-1])%mod)
            cache['o'].append((cache['i'][i-1])%mod)
            cache['u'].append((cache['o'][i-1]+cache['i'][i-1])%mod)
        return sum([cache[i][n-1] for i in cache])%mod