# Solution to https://leetcode.com/problems/largest-values-from-labels
from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        value_label = sorted(zip(values, labels), reverse = True, key = lambda pair: pair[0])
        labels_in_use = defaultdict(int)
        total_value = 0
        total_items = 0
        for i, val in enumerate(value_label):
            if labels_in_use.get(val[1],0) < useLimit:
                total_value += val[0]
                total_items += 1
                labels_in_use[val[1]] += 1
            if total_items == numWanted:
                break
        return total_value