# https://leetcode.com/problems/minimum-window-substring/

# 4.17.2023 ####### -> Hard question
# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
def minWindow(s,t):
  #create countT
  countT = {}
  for c in t:
      countT[c] = 1+countT.get(c,0)
  #create sliding window {}
  window = {}
  l = 0
  res, resLen = [-1,-1],float("inf")
  have, need = 0, len(countT)
  for r in range(len(s)):
      window[s[r]] = 1+ window.get(s[r],0)
      if s[r] in countT and window[s[r]] == countT[s[r]]:
          have +=1
      while have == need:
          #update the result
          if (r-l+1) <resLen:
              res = [l, r]
              resLen = r-l+1
          #remove the left
          window[s[l]] -=1
          if s[l] in countT and window[s[l]] < countT[s[l]]:
              have -= 1
          l+=1
  (l, r) =res
  return s[l : r + 1] if resLen != float("infinity") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))
