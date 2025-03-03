"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if len(stack) > 0 else i
                max_area = max(max_area,h*w)
            stack.append(i)
        while len(stack) > 0:
            h = heights[stack.pop()]
            if len(stack) > 0:
                w = len(heights) - stack[-1] - 1
            else:
                w = len(heights)
            max_area = max(max_area,h*w)
        return max_area

    def largestRectangleAreaBruteForce(self, heights: List[int]) -> int:
        max_rectangle = 0
        for i in range(len(heights)):
            for j in range(i, -1, -1):
                rect_size = min(heights[j:i+1])*(i-j+1)
                if max_rectangle < rect_size:
                    max_rectangle = rect_size
        return max_rectangle

        