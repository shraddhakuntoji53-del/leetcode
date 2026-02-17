class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(open_cnt, close_cnt, path):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            if open_cnt < n:
                path.append("(")
                backtrack(open_cnt + 1, close_cnt, path)
                path.pop()
            
            if close_cnt < open_cnt:
                path.append(")")
                backtrack(open_cnt, close_cnt + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
