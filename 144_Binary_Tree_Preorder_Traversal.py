# Recursive
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

# Iterative
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]

        if not root:
            return res

        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return res 
