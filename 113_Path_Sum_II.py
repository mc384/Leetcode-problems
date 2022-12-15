# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(node, cur):
            if not node:
                return
            cur.append(node.val)
            if not node.left and not node.right:
                if sum(cur) == targetSum:
                    self.res.append(cur.copy())
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
            cur.pop()
            print(cur)
        dfs(root, [])
        return self.res 
