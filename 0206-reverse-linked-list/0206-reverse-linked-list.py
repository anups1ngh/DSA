# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = prev
        return new_head