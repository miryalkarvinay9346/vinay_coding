class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        """ 
        s=len(nums)*(len(nums)+1)//2
        a=sum(set(nums))
        return s-a
        