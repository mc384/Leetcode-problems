# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        while current: 
            if p == current or q == current:
                return current 
            if (p.val > current.val and q.val < current.val) or (p.val < current.val and q.val > current.val):
                return current
            if p.val > current.val and q.val > current.val:
                current = current.right 
            else:
                current = current.left 
        # Time: O(n)
        # Space: O(1)
