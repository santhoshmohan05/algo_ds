# https://leetcode.com/problems/house-robber-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## for each node there are 2 options.
#       -> we can add present node, then cannot add child nodes
#       -> we can omit present node, then can return maximum return from the child node max(with, without)
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0,0
            left_with, left_without = dfs(root.left)
            right_with, right_without = dfs(root.right)
            without = max(left_with, left_without) + max(right_with, right_without)
            with_val = root.val + left_without + right_without
            return with_val, without
        return max(dfs(root))
