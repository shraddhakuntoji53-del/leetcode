class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        # Helper to find middle of linked list
        def findMid(head):
            prev = None
            slow = fast = head
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            # Disconnect left half
            if prev:
                prev.next = None
            
            return slow
        
        # Base case
        if not head:
            return None
        
        # Find middle node
        mid = findMid(head)
        
        # Make middle the root
        root = TreeNode(mid.val)
        
        # If only one element
        if head == mid:
            return root
        
        # Recursively build left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
