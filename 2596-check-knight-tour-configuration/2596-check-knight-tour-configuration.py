class Solution:
    def checkValidGrid(self, grid):
        n = len(grid)
        
        # 0 must start at top-left
        if grid[0][0] != 0:
            return False
        
        # store positions of each number
        pos = [None] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i, j)
        
        # all possible knight moves
        moves = {
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        }
        
        # verify each step
        for i in range(n * n - 1):
            r1, c1 = pos[i]
            r2, c2 = pos[i + 1]
            if (r2 - r1, c2 - c1) not in moves:
                return False
        
        return True
