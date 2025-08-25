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
     
import numpy as np
class Solution():
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        np.concatination(nums1,nums2)    