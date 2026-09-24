# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        first = head
        length = 0

        while curr:
            curr = curr.next
            length+=1
        
        remove = length - n

        if remove == 0:
            return head.next

        curr = head
        count = 0

        while count < remove-1:
            curr = curr.next
            count+=1
        
        curr.next = curr.next.next

        return head
        
        


            



