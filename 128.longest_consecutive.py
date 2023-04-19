#4.12.2023
def longestConsecutive(nums):
  num_set = set(nums)
  longest = 0
  for num in nums:
    #check if the left item in the list
    if (num-1) not in num_set:
      length = 0
      while (num+length) in num_set:
        length+=1
      longest = max(longest,length)
  return longest

print(longestConsecutive([14,22,23,25,21,2,3,6,7]))

