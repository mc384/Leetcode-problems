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
        if not p:
            if not q:
                return True
            else:
                return False
        if not q:
            if not p:
                return True
            else:
                return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
## Test Cases
# isSameTree([], []) returns True
# isSameTree([1,2,3,4], [1,2,3]) returns False
# isSameTree([1, null, null], [1, null, null]) returns True
