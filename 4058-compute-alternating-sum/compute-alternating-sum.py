class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        se=0
        so=0
        for i in range(0,len(nums)):
            if(i%2==0):
                se+=nums[i]
            else:
                so+=nums[i]
        return se-so        
