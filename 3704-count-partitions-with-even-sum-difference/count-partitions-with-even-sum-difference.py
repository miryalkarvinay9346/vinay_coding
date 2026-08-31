class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            a=nums[:i]
            b=nums[i:]
            if (sum(a)-sum(b))%2==0:
                c+=1
        return c