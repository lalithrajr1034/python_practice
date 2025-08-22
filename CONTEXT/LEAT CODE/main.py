class Solution(object):
    def twoSum(self, nums, target):
        for i in range(nums):
            for j in range(nums):
                if nums[i]+nums[j] == target:
                    return [nums[i],nums[j]]
                
li = [3,2,4]
# a = Solution()
# print(a.twoSum(li, 6))

for i in range(len(li)):
    print(i)