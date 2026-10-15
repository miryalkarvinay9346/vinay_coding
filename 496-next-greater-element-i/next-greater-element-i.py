class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=[-1]*len(nums1)
        for i in range(len(nums1)):
            k=nums1[i]
            idx=nums2.index(k)
            for j in range(idx+1,len(nums2)):
                if nums2[j]>k:
                    a[i]=nums2[j]
                    break
        return a