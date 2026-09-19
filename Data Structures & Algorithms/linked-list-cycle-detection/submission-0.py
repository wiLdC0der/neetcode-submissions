# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        fastest = head
        while fastest and fastest.next:
                fast = fast.next
                fastest = fastest.next.next

                if fast == fastest:
                    return True
        return False

        