#4.12.2023
import collections

# method1
def groupAnagrams(strs):
  ans = collections.defaultdict(list)

  for s in strs:
    count = [0]*26
    for c in s:
      count[ord(c)-ord("a")]+=1
    # print("count: ",count)
    ans[tuple(count)].append(s)
    print("ans: ", ans)

  return ans.values()

# method2
def groupAnagrams(strs):
  hashmap = {}
  for str in strs:
      str1 = ''.join(sorted(str))
      if str1 not in hashmap:
          hashmap[str1] = []
      hashmap[str1].append(str)

  return list(hashmap.values())
print(groupAnagrams(["eat","tea","tae","abc"]))

