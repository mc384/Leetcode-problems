class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSym(root1, root2):
            if not root1 and not root2:
                return True
            if not root1: 
                return False
            if not root2:
                return False 
            if root1.val != root2.val:
                return False 
            return checkSym(root1.left, root2.right) and checkSym(root1.right, root2.left)
        return checkSym(root.left, root.right)
