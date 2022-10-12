# https://leetcode.com/problems/combination-sum/
from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def append_answer(answer, target, candidate):
            prev_list = answer[target - candidate]
            for ps in prev_list:
                answer[target].append(ps.copy()+[candidate])

        answer = defaultdict(list)
        for i in candidates:
            for j in range(i,target+1):
                if j - i == 0:
                    answer[j].append([i])
                elif j - i > 0:
                    append_answer(answer,j,i)
        return answer[target]