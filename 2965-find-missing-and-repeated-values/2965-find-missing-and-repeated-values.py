class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        
        freq = [0] * (size + 1)
        
        for row in grid:
            for num in row:
                freq[num] += 1
        
        repeated = missing = 0
        
        for i in range(1, size + 1):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i
        
        return [repeated, missing]
