class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c=0
        for i in set(nums):
            if nums.count(i)==2:
                c=c^i
        return c