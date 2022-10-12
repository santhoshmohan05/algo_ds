## https://practice.geeksforgeeks.org/problems/preorder-traversal-and-bst4006/
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