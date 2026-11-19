# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res, stack, visited = [], [root], [False]
        
        while stack:
            node, v = stack.pop(), visited.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    
                    stack.append(node.right)
                    visited.append(False)
                    stack.append(node.left)
                    visited.append(False)
                    stack.append(node)
                    visited.append(True)
        return res
        