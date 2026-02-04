from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, path):
            res.append(path[:])      # store a copy
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()           # undo choice
        
        backtrack(0, [])
        return res
