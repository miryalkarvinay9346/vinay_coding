class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                k=nums[i:j+1]
                s+=len(set(k))**2
        return (s)