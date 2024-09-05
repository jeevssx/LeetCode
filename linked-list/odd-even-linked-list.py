# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        even = head
        odd = head.next
        odd_head = head.next
        while odd and odd.next:
            even.next = even.next.next
            even = even.next
            odd.next = odd.next.next
            odd = odd.next
        even.next = odd_head
        return head
            