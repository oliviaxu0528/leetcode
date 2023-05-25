def generateParenthesis(n):
    # only add open paranthesis if open<n
    # only add a closing paranthesis if close<open
    # valid IIF open == closed == n
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            print("stack0:", stack)
            res.append("".join(stack))
            print("res0:", res)

        if openN < n:
            stack.append("(")
            backtrack(openN+1, closedN)
            print("stack1", stack)
            stack.pop()

        if openN > closedN:
            stack.append(")")
            backtrack(openN, closedN+1)
            print("stack2:", stack)
            stack.pop()

    backtrack(0, 0)
    print("res: ", res)
    return res


generateParenthesis(3)
