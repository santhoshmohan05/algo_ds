# https://leetcode.com/problems/time-needed-to-inform-all-employees/

from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        informMaxTime = [0]*len(manager)
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        queue = [headID]

        while queue:
            idx = queue.pop(0)
            informMaxTime[idx] = informTime[idx] + informMaxTime[manager[idx]]
            for child in graph[idx]:
                queue.append(child)
        return max(informMaxTime)