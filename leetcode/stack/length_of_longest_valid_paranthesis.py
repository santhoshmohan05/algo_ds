"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring.

Leetcode: https://leetcode.com/problems/longest-valid-parentheses/description/
"""

# Adding comment to test the git oush
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        answer = 0
        prev_count = []
        curr_count = 0
        for chr in s:
            if chr == "(":
                prev_count.append(curr_count)
                curr_count = 0
                stack.append(chr)
            elif chr == ")":
                if stack and stack[-1] == "(":
                    curr_count += 2
                    if prev_count:
                        curr_count += prev_count.pop()
                    stack.pop()
                    if curr_count > answer:
                        answer = curr_count
                else:
                    curr_count = 0
        return answer
        