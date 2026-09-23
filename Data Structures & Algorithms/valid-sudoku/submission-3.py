class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                
                num = board[i][j]

                box = (i // 3) * 3 + (j // 3)

                if num in rows[i]:
                    return False
                if num in column[j]:
                    return False
                if num in grid[box]:
                    return False
                
                rows[i].add(num)
                column[j].add(num)
                grid[box].add(num)
        return True