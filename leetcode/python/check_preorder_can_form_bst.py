## https://practice.geeksforgeeks.org/problems/preorder-traversal-and-bst4006/
## monotonic stack, have a non-increasing stack
## pop all elements lower than incoming value and name last poped as root

class Solution:
    def canRepresentBST(self, arr, N):
        # code here
        stack = []
        root = -1
        for num in arr:
            if num < root:
                return 0
            while stack and stack[-1] < num:
                root = stack.pop()
            stack.append(num)
        return 1
