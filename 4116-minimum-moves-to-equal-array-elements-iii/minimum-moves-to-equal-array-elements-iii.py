class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        c=0
        for i in range(len(nums)):
            c+=m-nums[i]
        return (c)    
        