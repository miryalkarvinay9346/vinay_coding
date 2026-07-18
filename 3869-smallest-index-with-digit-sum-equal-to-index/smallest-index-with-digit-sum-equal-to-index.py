class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            s=0
            k=nums[i]
            while k>0:
                s+=k%10
                k//=10
            if s==i:
                return i
        return -1        

        