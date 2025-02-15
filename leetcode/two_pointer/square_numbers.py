"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
Leetcode: https://leetcode.com/problems/squares-of-a-sorted-array/description/
"""

class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    i = 0
    j = n-1
    k = n-1
    while i <= j:
      if abs(arr[i]) > abs(arr[j]):
        squares[k] = arr[i] * arr[i]
        i += 1
      else:
        squares[k] = arr[j] * arr[j]
        j -= 1
      k -= 1
    return squares