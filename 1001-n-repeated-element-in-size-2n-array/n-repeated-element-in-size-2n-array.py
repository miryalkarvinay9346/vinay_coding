class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n=len(nums)//2
        for i in nums:
            if nums.count(i)==n:
                return i
        return -1