class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            k=nums[i]
            s=0
            while k>0:
                s=s+k%10
                k=k//10
            nums[i]=s
        return min(nums)            



        