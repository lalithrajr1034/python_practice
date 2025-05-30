class Solution:
    def twoSum(self, lis ,target):
        for i in range(0,len(lis)-2):
            if lis[i]==target:
                print(f"[{i}]")
            elif (lis[i]+lis[i+1])==target:
                print(f"[{i},{i+1}]") 
            elif (lis[i]+lis[i+2])==target:
                print(f"[{i},{i+2}]")         



nums=[2,7,11,15]
target=9
obj=Solution()
b=obj.twoSum(nums,target)


class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Stores value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
