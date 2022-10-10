# https://leetcode.com/problems/reconstruct-itinerary/
# Hierholzer’s Algorithm  -> Finding eulers path.

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u,v in tickets:
            graph[u].append(v)
        for vertices in graph:
            graph[vertices] = sorted(graph[vertices], reverse = True)
        result = []
        
        def dfs(u):
            nonlocal graph, result
            while graph[u]:
                dfs(graph[u].pop())
            result.append(u)
        dfs("JFK")
        return result[::-1]
        