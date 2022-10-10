# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def createParentMap(root,graph,parent):
            if not root:
                return
            graph[root] = parent
            createParentMap(root.left,graph,root)
            createParentMap(root.right,graph,root)

        def find_node(root, value):
            if not root:
                return None
            if root.val == value:
                return root
            left = find_node(root.left, value)
            if left:
                return left
            right = find_node(root.right, value)
            if right:
                return right

        target = find_node(root,start)
        parent_map = {}
        createParentMap(root,parent_map,None)
        
        visited = set()
        def dfs(root,visited,parent_map):
            if not root:
                return 0
            if root in visited:
                return 0
            # print(root.val, [x.val for x in visited])
            visited.add(root)
            left = dfs(root.left,visited,parent_map)
            right = dfs(root.right,visited,parent_map)
            parent = 0
            if parent_map[root]:
                parent = dfs(parent_map[root],visited,parent_map)
                
            return max(left, right, parent) + 1
        
        return dfs(target, visited, parent_map) - 1
            
            
        
            
            
            