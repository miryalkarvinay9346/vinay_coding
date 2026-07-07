class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    k=(nums[i]-1)*(nums[j]-1)
                    c=max(c,k)
        return c
        