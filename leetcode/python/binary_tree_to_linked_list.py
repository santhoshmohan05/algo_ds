# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        last_node = self.flattenRecur(root)
        return root
    
    def flattenRecur(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left = root.left
        right = root.right
        root.left = None # change root.eft to None
        ## flatten left side if present and add to root.right
        if left:
            left_last_node = self.flattenRecur(left)
            root.right = left
        else:
            left_last_node = root
        ## flatten right side and add to last node after left flatten
        if right:
            right_last_node = self.flattenRecur(right)
            left_last_node.right = right
        else:
            right_last_node = left_last_node
        ## return the last node of this tree
        return right_last_node
    
    def flattenSimpleRecur(self, root):
        if not root:
            return root
        self.flattenSimpleRecur(root.right)
        self.flattenSimpleRecur(root.left)
        root.left = None
        root.right = self.prev
        self.prev = root