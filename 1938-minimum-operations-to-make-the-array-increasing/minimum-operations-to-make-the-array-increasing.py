class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                n=nums[i-1]+1
                c+=n-nums[i]
                nums[i]=n
        return c
