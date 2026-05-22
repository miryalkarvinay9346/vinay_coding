class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            a.append(nums[i])
        for j in range(len(nums)):
            a.append(nums[len(nums)-j-1])    
        return a

        