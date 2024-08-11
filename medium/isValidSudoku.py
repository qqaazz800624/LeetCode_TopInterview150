#%%

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    if num in row_sets[i] or num in col_sets[j] or num in box_sets[i//3*3+j//3]:
                        return False
                    row_sets[i].add(num)
                    col_sets[j].add(num)
                    box_sets[i//3*3+j//3].add(num)
        return True

#%%
row_sets = [set() for _ in range(9)]

row_sets[0].add(1)
row_sets

#%%