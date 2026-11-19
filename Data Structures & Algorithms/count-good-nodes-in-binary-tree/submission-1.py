# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, -float('inf'))])
        res = 0
        while q:
            node, mx = q.popleft()

            if node.val >= mx:
                res += 1
            if node.left:
                q.append((node.left, max(mx, node.val)))
            if node.right:
                q.append((node.right, max(mx, node.val)))
        
        return res