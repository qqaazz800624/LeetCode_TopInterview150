#%%

from typing import List
from collections import deque

class Solution:
    def getCoordinates(self, square):  # Converts 1D square number to 2D (row, col) on the board
        row = (square - 1) // self.n
        col = (square - 1) % self.n

        if row % 2 == 0:
            return (self.n - 1 - row, col) # normal left to right
        else:
            return (self.n - 1 - row, self.n - 1 - col) # reverse right to left

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.n = len(board)

        # Initialize the BFS queue and visited set
        #queue = [(1, 0)] # (current square, number of moves)
        queue = deque([(1, 0)])  # (current square, number of moves)
        visited = set()

        while queue:
            #square, moves = queue.pop(0)
            square, moves = queue.popleft()

            # If we have reached the final square
            if square == self.n * self.n:
                return moves
            
            # Try all dice rolls from 1 to 6

            for i in range(1, 7):
                next_square = square + i
                if next_square > self.n * self.n:
                    continue

                row, col = self.getCoordinates(next_square)

                # Check if there is a ladder or a snake
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                # If the square has not been visited yet, add it to the queue
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1 # If no solution is found

        


#%%







#%%








#%%