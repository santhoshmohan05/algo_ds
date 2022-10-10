# https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        Greedy Approach works here, since any two negative numbers in any position can be turned to positive 
        using a series of operations. 
        e.g. -> [1,1,-3]
                [1,1,1]    both -3 can be turned to positive using a series of operation by multiplying
                [-3,1,1]   adjacent values to -1  (since all the values will be multiplied twice with -1)
        
        So need, if even number of negative numbers in martix can return sum, else sum - min(abs(value))
        if there is zero in matric, then can convert all the negative values to positive
        """
        total = 0
        minimum = float('Inf')
        has_zero = False
        total_negative = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                total += abs(matrix[i][j])
                if  matrix[i][j] == 0:
                    has_zero = True
                minimum = min(minimum, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    total_negative += 1
        
        if has_zero or total_negative %2 == 0:
            return total
        else:
            return total - 2*minimum