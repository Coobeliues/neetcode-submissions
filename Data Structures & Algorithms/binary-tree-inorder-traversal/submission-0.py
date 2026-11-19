# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inord(node):
            if node is None:
                return
            inord(node.left)
            res.append(node.val)
            inord(node.right)

        res = []
        inord(root)
        
        return res