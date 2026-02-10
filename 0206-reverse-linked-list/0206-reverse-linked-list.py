class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save next
            curr.next = prev     # reverse pointer
            prev = curr          # move prev
            curr = nxt           # move curr

        return prev
