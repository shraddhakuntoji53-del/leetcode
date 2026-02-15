class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while True:
            # Go to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process node
            curr = stack.pop()
            k -= 1
            
            if k == 0:
                return curr.val
            
            # Move to right subtree
            curr = curr.right
