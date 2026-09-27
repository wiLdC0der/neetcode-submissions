# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        result = []
        curr = l1
        seccurr = l2

        while curr and seccurr:
            total = curr.val + seccurr.val + carry

            carry = total // 10
            result.append(total % 10)

            curr = curr.next
            seccurr = seccurr.next

        while curr:
            total = curr.val + carry
            carry = total // 10
            result.append(total % 10)
            curr = curr.next

        while seccurr:
            total = seccurr.val + carry
            carry = total // 10
            result.append(total % 10)
            seccurr = seccurr.next


        if carry:
            result.append(carry)

        dummy = ListNode(0)
        curr = dummy

        i = 0
        while i < len(result):
            curr.next = ListNode(result[i])
            curr = curr.next
            i += 1

        return dummy.next

        
        