# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []

        def valid(node):
            if not node:
                return
            valid(node.left)
            a.append(node.val)
            valid(node.right)
        
        valid(root)

        return a[k - 1]
