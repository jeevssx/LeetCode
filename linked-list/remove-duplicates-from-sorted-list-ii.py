# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tempNode = ListNode(0, head)

        fastPtr = head
        slowPtr = tempNode
       
        while fastPtr:
            
            while fastPtr.next and fastPtr.val == fastPtr.next.val:
                
                fastPtr = fastPtr.next
            
            if slowPtr.next == fastPtr:
                
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next
            
            else:
                slowPtr.next = fastPtr.next
                fastPtr = slowPtr.next
        
        return tempNode.next

            