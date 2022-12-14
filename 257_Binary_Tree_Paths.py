# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        cur = ""

        def dfs(node, cur):
            if not node:
                return
            if node:
                if not node.left and not node.right:
                    cur += str(node.val)
                    res.append(cur)
                else:
                    cur += str(node.val)
                    cur += "->"
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
            print(cur)
        
        dfs(root, cur)
        return res 
 # Time: O(n)
 # Space: O(log n)
