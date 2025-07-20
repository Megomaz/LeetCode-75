# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if slow != fast:
            prev.next = slow.next
            return head
        else:
            return None


       
# Slightly better logic for length = 1
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next
        return head