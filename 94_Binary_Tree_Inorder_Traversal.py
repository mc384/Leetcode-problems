# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, cur):
            if not node:
                return
            if node.left:
                dfs(node.left, cur)
            cur.append(node.val)
            if node.right:
                dfs(node.right, cur)
            return cur
        
        return dfs(root, [])
