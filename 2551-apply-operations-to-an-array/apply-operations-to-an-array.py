class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        p=0
        for k in range(len(nums)):
            if nums[k]!=0:
                nums[p],nums[k]=nums[k],nums[p]
                p+=1
        return nums
        