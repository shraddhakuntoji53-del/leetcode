class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # initialize sets
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)
        
        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != ".":
                return backtrack(r, c + 1)
            
            box_id = (r // 3) * 3 + c // 3
            for ch in "123456789":
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_id]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_id].add(ch)
                    
                    if backtrack(r, c + 1):
                        return True
                    
                    # backtrack
                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_id].remove(ch)
            
            return False
        
        backtrack(0, 0)
