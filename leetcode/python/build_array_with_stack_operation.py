# https://leetcode.com/problems/build-an-array-with-stack-operations
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return []
        if n <= 0:
            return []
        output = []
        stack = []
        for i in range(1,n+1):
            output.append("Push")
            stack.append(i)
            if target == stack:
                return output
            if i not in target:
                stack.pop()
                output.append("Pop")
        return output
        