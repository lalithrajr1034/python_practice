class Solution():
    @staticmethod
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [nums[i],nums[j]]
                
li = [3,2,4]
a = Solution()
print(a.twoSum(li, 6))