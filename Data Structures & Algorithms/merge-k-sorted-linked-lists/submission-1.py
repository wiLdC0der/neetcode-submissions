# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for lst in lists:
            while lst:
                result.append(lst.val)
                lst = lst.next
        
        result.sort()

        newlist = ListNode(0)
        curr = newlist

        for num in result:
            curr.next = ListNode(num)
            curr = curr.next
        
        return newlist.next

