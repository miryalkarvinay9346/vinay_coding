class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        for i in range(a):
            nums.remove(0)
            nums.append(0)