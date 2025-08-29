# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashmap={}
#         for i,n in enumerate(nums):
#             diff=target-n
#             if diff in hashmap:
#                 return [hashmap[diff],i]
#             hashmap[n]=i
#         return
     
class Solution():
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        val = sorted(nums1+nums2)
        a = len(val)
        odd = a//2
        if a%2 == 0:
            return (val[odd-1]+val[odd])/2
        else:
            return val[odd]      

a = Solution
print(a.findMedianSortedArrays([1,2],[3,4]))
        
print((3+2)/2)       