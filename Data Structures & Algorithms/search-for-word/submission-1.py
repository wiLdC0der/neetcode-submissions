class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row = len(board)
        column = len(board[0])
        ans = ""

        def backtrack(i,j,k):
            if k == len(word):
                return True
            

            if i < 0 or i >= row or j < 0 or j>= column:
                return False 
            
            if board[i][j] != word[k]:
                return False
          
            temp = board[i][j]
            board[i][j] = "#"

            found = (
                backtrack(i + 1, j, k + 1) or
                backtrack(i - 1, j, k + 1) or
                backtrack(i, j + 1, k + 1) or
                backtrack(i, j - 1, k + 1)
            )

            board[i][j] = temp

            return found
        for i in range(row):
            for j in range(column):
                if backtrack(i,j,0):
                    return True
        return False



                

