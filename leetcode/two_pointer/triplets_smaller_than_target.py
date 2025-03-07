
"""
Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.
"""

class Solution:
  def searchTriplets(self, arr, target):
    count = 0
    # TODO: Write your code here
    arr.sort()
    i = 0
    while i < len(arr)-2:
      left = i + 1
      right = len(arr) -1
      while left < right:
        if arr[i] + arr[left] + arr[right] < target:
          count += right - left
          left += 1
        else:
          right -= 1
      i += 1
    return count
