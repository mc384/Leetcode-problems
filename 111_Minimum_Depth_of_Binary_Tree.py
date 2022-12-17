# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left:
            left = 1 + self.minDepth(root.left)
        if not root.left:
            left = float("inf")
        if root.right:
            right = 1 + self.minDepth(root.right)
        if not root.right:
            right = float("inf")
        print(left, right)
        return min(left, right)
