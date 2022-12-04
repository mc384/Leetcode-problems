class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        def dfs(node, arr):
            if node.left:
                dfs(node.left, arr)
            if node.right:
                dfs(node.right, arr)
            arr.append(node.val)
            
        dfs(root, res)
        return res 
