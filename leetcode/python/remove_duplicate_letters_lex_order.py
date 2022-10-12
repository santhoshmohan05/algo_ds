# https://leetcode.com/problems/remove-duplicate-letters/
## greedy approac and using monotonic stack to keep lexological order
## counter before so that we know of a char is present in the remaining string

from collections import defaultdict, Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        taken = set()
        stack = []
        for char in s:
            if char not in taken:
                ## count check to know if same char is appearing again later in string
                while stack and stack[-1] > char and count[stack[-1]] > 0:
                    prev_char = stack.pop()
                    taken.remove(prev_char)
                stack.append(char)
                taken.add(char)
            count[char] -= 1
        return "".join(stack)