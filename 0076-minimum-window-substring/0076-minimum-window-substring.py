from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        need = Counter(t)
        window = {}
        
        required = len(need)
        formed = 0
        
        l = 0
        min_len = float('inf')
        min_window = (0, 0)
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)
                
                left_char = s[l]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                
                l += 1
        
        l, r = min_window
        return "" if min_len == float('inf') else s[l:r+1]
