# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        backward = None

        while cur != None:
            forward = cur.next
            cur.next = backward

            backward = cur
            cur = forward

        return backward
