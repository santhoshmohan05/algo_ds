# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def create_graph(self, root,graph, parent):
        if not root:
            return 
        graph[root] = []
        if parent:
            graph[root].append(parent)
        if root.left:
            graph[root].append(root.left)
            self.create_graph(root.left, graph,root)
        if root.right:
            graph[root].append(root.right)
            self.create_graph(root.right, graph,root)
            
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        result = []
        graph = {}
        self.create_graph(root,graph,None)
        queue = [(target,0)]
        visited = set()
        while queue:
            node, distance = queue.pop(0)
            visited.add(node)
            if distance == k:
                result.append(node.val)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append((nei,distance+1))
        return result
                