from collections import deque
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        left_to_right = True
        
        while q:
            level_size = len(q)
            level = []
            
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not left_to_right:
                level.reverse()
            
            res.append(level)
            left_to_right = not left_to_right
        
        return res
