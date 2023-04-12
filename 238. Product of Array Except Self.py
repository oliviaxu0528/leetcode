#4.12.2023
def productExceptSelf(nums):
    res = [1]*len(nums)

    prefix = 1
    for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]

    # res ->[1,2,6,24]

    postfix = 1
    for j in range(len(nums)-1,-1,-1):
      res[j] *= postfix
      postfix *= nums[j]

    return res

print(productExceptSelf([2,3,4,1]))
#[3*4*4]
