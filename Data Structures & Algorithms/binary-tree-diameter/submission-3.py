# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        mp = {None: (0, 0)}
        stack = [root]

        while stack:
            node = stack[-1]
            
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                l, ld = mp[node.left]
                r, rd = mp[node.right]

                mp[node] = (1 + max(l, r), max(l + r, ld, rd))

        return mp[root][1]