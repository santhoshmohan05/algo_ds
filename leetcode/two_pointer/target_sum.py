"""
Given an array of numbers sorted in ascending order and a target sum, 
find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) 
such that they add up to the given target. If no such pair exists return [-1, -1].
"""

def search( arr, target_sum):
    if len(arr)<2:
        return[-1, -1]
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left] + arr[right] == target_sum:
            return[left, right]
        elif arr[left] + arr[right] > target_sum:
            right -=1
        else:
            left +=1
    return [-1, -1]