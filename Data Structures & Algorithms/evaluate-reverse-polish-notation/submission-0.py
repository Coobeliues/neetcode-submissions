class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = []
        for token in tokens:
            if token in '-+*/':
                right = a.pop()
                left = a.pop()

                if token == '+':
                    a.append(left + right)
                elif token == '-':
                    a.append(left - right)
                elif token == '*':
                    a.append(left * right)
                else:
                    a.append(int(left / right))
            else:
                a.append(int(token))
        
        return a[0]