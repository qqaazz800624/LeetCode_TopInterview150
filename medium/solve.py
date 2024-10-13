#%%

from typing import List

class Solution:
    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == 'O':
            board[i][j] = 'S'
            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i, j - 1)
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        rows = len(board)
        cols = len(board[0])

        # step 1: Mark the safe regions (connected to the border)
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    self.dfs(board, i, j)

        # step 2: Capture surrounded regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'




#%%






#%%






#%%