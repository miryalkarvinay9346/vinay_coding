class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        a=min(nums)
        b=max(nums)
        for i in nums:
            if i!=a and i!=b:
                return i
        return -1