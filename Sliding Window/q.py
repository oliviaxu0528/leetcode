count = {}
A = "abbccdf"
for c in A:
    count[c] = 1+count.get(c, 0)

print("count: ", len(count))
