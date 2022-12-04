# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        if not root:
            return arr 
        def dfs(node, visited):
            visited.append(node.val)
            if node.left:
                dfs(node.left, visited)
            if node.right:
                dfs(node.right, visited)
        dfs(root, arr)
        return arr
