# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Problem lends itself well to recursion
## Depth-first search
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True  
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False 
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

