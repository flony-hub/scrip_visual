class Solution:
    def findMedianaSortedArray(self, nums1, nums2):
        nums3 = nums1 + nums2
        return print(sum(nums3) / len(nums3)) 



nums1 = [1,5,3,4,2,3,6,4,6,9]
nums2 = [7,8,]
ver = Solution()
ver.findMedianaSortedArray(nums1, nums2)