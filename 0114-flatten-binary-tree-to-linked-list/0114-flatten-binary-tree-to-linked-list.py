class Solution:
    def flatten(self, root):
        curr = root
        
        while curr:
            if curr.left:
                # find rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # rewire pointers
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right
