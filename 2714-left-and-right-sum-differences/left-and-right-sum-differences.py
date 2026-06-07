class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return [0]
        l=[0]*len(nums)
        r=[0]*len(nums)
        lsum=rsum=0
        ans=[]
        for i in range(len(nums)):
            l[i]=lsum
            lsum+=nums[i]
        for j in range(len(nums)-1,-1,-1):
            r[j]=rsum
            rsum+=nums[j]
        for k in range(0,len(l)):
            ans.append(abs(l[k]-r[k]))    
        return ans    

        
