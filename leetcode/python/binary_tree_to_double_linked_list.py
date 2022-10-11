# https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/
class Solution:
    def __init__(self):
        self.prev = None
        self.head = None
    def bToDLL(self,root):
        # do Code here
        def recur(root):
            if not root:
                return root
            recur(root.left)
            root.left = self.prev
            if self.prev:
                self.prev.right = root
            else:
                self.head = root
            self.prev = root
            recur(root.right)
        recur(root)
        return self.head