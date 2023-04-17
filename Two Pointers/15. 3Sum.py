# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # sort the nums
    nums.sort()
    print(nums)
    # take the first one, loop through the rest as a two sum
    res = []
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left < right:
            if nums[left]+nums[right] == -nums[i]:
                res.append([nums[left], nums[right], nums[i]])
            elif nums[left]+nums[right] + nums[i] < 0:
                left += 1
            else:
                right -= 1

    # print("res: ": res)
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
