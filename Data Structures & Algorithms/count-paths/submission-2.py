class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}
        def backtrack(i,j):
            
            if i == m-1 and j == n-1:
                return 1
            
            if (i,j) in memo:
                return memo[i,j]
            if i >= m or j >= n:
                return 0
            down = backtrack(i+1,j)
            right = backtrack(i,j+1)
            memo[i, j] = down + right
            return down + right
        return backtrack(0,0)