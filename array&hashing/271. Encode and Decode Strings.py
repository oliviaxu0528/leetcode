def encode(strs):
    """Encodes a list of strings to a single string.

    :type strs: List[str]
    :rtype: str
    """
    s = ""
    for string in strs:
        s += str(len(string))+"#" + string
    return s


y = encode(["Hello", "World"])
print(encode(["Hello", "World"]))


def decode(s):
    """Decodes a single string to a list of strings.

    :type s: str
    :rtype: List[str]
    """
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
            length = int(s[i:j])
        char = s[j+1:j+1+length]
        res.append(char)
        i = j+1+length
    return res


print(decode(y))
