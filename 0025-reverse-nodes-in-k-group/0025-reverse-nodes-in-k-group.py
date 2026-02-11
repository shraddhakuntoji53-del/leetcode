# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # Step 1: Check if there are k nodes left
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next

            # Step 2: Reverse k nodes
            prev = next_group
            curr = prev_group.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 3: Connect with previous part
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp
