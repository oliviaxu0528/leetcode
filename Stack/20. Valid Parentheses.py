# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

def isValid(s):
  #create stack
  dic = {')':'(',"}":"{","]":"["}
  stack = []
  for c in s:
    if c in dic:
        if stack and stack[-1] == dic[c]:
            print("stack: ",stack)
            stack.pop()
        else:
            return False
    else:
        stack.append(c)
  return not stack

s = "()"
print(isValid(s))