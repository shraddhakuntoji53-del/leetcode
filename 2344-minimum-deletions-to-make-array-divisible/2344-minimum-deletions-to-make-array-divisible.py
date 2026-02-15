from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # Step 1: Compute gcd of numsDivide
        g = numsDivide[0]
        for num in numsDivide:
            g = math.gcd(g, num)
        
        # Step 2: Sort nums
        nums.sort()
        
        # Step 3: Find smallest nums[i] that divides g
        for i, num in enumerate(nums):
            if g % num == 0:
                return i   # i deletions needed
        
        return -1
