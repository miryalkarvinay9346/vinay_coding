class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sorted(set(nums))
        for i in range(len(a)):
            nums[i]=a[i]
        return len(a)
        