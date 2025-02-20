"""
Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/description/
"""

from typing import List
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initially, each node is its own parent
        self.rank = [1] * size  # Rank (depth of trees)

    def find(self, x):
        if self.parent[x] != x:  # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootY != y:
            return
        else:
            self.parent[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(c) for c in favoriteCompanies]
        n = len(sets)
        uf= UnionFind(n)
        for i in range(n):
            for j in range(n):
                if i != j and sets[i] < sets[j]:
                    uf.union(j,i)
        return sorted(set([uf.find(i) for i in range(n)]))
