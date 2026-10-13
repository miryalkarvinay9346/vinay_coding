class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        s=0
        for i in nums:
            if nums.count(i)%k==0:
                s+=i
        return s