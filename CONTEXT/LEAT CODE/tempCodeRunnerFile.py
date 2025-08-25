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
        