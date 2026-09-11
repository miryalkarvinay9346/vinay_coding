class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        w=nums[0]
        x=nums[1]
        y=nums[-1]
        z=nums[-2]
        return ((w*x)-(y*z))