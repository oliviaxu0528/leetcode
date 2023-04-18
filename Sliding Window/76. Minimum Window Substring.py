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
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if t == "":
        return ""
    countT = {}
    window = {}

    for char in t:
        countT[char] = 1 + countT.get(char, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1+window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            # update out result
            if (r-l+1) < resLen:
                res = [l, r]
                resLen = r-l+1

            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    print("res: ", res)
    # l, r = res

    print("l, r ", (l, r))
    print("s[l:r+1]: ", s[l:r+1])
    return s[l-1:r+1] if resLen != float("inf") else ""


s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))
