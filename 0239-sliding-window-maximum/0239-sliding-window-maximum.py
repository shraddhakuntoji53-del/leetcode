from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # remove out-of-window indices
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # window starts from index k - 1
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
