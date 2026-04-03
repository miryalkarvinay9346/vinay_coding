class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        p=1
        for i in range(len(nums)):
            p*=nums[i]
        if p>0:
            return 1
        elif p==0:
            return 0
        else:
            return -1       
        """
        p=math.prod(nums)
        if p>0:
            return 1
        elif p==0:
            return 0
        else:
            return -1        

        