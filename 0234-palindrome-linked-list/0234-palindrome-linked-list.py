class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # store next
            curr.next = prev     # reverse pointer
            prev = curr
            curr = nxt

        return prev