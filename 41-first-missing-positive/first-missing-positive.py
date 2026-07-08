class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        e=1 #expecting initially 1 as missing digit 
        for i in range(len(nums)):
            if nums[i]<=0:
                continue
            else:
                if nums[i]==e: #if intial digit is found
                    e+=1        # then increment 
                elif nums[i]>e:
                    return e
        return e            
        