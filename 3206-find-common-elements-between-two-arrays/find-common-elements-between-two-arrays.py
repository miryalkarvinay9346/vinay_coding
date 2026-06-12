class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a,b=0,0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                a+=1
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                b+=1
        return [a,b]            
        