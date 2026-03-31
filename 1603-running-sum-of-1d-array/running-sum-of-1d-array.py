class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        a=[]
        for i in range(len(nums)):
            sum+=nums[i]
            a.append(sum)
        return a    
        