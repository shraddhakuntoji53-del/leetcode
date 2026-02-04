from typing import List

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Map end index → required inversion count
        req = {end: cnt for end, cnt in requirements}
        max_inv = 400
        
        # dp[j] = number of ways for current prefix with j inversions
        dp = [0] * (max_inv + 1)
        dp[0] = 1
        
        for i in range(1, n):
            new_dp = [0] * (max_inv + 1)
            prefix = [0] * (max_inv + 2)
            
            # prefix sum of dp
            for j in range(max_inv + 1):
                prefix[j + 1] = (prefix[j] + dp[j]) % MOD
            
            # compute transitions
            for j in range(max_inv + 1):
                left = max(0, j - i)
                right = j
                new_dp[j] = (prefix[right + 1] - prefix[left]) % MOD
            
            # apply requirement if exists
            if i in req:
                cnt = req[i]
                filtered = [0] * (max_inv + 1)
                if cnt <= max_inv:
                    filtered[cnt] = new_dp[cnt]
                new_dp = filtered
            
            dp = new_dp
        
        # final requirement must exist at n-1
        return sum(dp) % MOD
