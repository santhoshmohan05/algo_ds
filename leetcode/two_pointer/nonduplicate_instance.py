"""
Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place.
The non-duplicate numbers should be sorted and you should not use any extra space so that the solution has constant space complexity i.e., .

Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.
"""

class Solution:
  def moveElements(self, arr):
    key = 0
    for i in range(1,len(arr)):
      if arr[i] != arr[key]:
        key += 1
        arr[key] = arr[i]
    return key+1