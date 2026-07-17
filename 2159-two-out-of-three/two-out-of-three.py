class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        a=[]
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set(nums3)
        for  i in  nums1.union(nums2).union(nums3):
            c=0
            if i in nums1:
                c+=1
            if i in nums2:
                c+=1
            if i in nums3:
                c+=1    
            if c>=2:
                a.append(i)
        return a    
