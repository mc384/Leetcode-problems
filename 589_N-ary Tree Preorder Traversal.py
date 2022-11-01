"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nums = []
        def traversal(root, nums):
            if not root:
                return None
            else:
                nums.append(root.val)
                for child in root.children:
                    traversal(child, nums)
            return nums

        return traversal(root, nums)
