class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        
        def dfs(opn, cls):
            if opn == n and cls == n:
                res.append(''.join(path))
                return
            
            if opn < n:
                path.append('(')
                dfs(opn + 1, cls)
                path.pop()
            
            if opn > cls:
                path.append(')')
                dfs(opn, cls + 1)
                path.pop()
        
        dfs(0, 0)

        return res