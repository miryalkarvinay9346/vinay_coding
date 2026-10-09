class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        a0=[]
        a1=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                if nums1[i] not in a0:
                    a0.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                if nums2[j] not in a1:
                    a1.append(nums2[j])
        return [a0,a1]
