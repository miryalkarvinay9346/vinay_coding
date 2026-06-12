class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k>0:
            m=min(nums)
            for i in range(len(nums)):
                if nums[i]==m:
                    nums[i]=nums[i]*multiplier
                    break
            k-=1
        return nums    
        