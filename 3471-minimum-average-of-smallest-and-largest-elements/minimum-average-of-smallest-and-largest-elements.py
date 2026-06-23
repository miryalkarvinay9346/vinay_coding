class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        while len(nums)>1:
            avg.append((max(nums)+min(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(avg)    
        