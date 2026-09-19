# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(first,second):
            if first is None or second is None:
                return first == second
            if first.val != second.val:
                return False
            
            left = dfs(first.left,second.left)
            right = dfs(first.right, second.right)

            return left and right
        return dfs(p,q)





        
        
        