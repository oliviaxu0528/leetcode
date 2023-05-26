# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtrack -> if open == close ==n, return res
        #if open <n, add (
        #if open >close, add )

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            
            if openN>closeN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        
        backtrack(0,0)
        return res

        
