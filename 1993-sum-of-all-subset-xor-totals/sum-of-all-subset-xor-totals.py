class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        c=0
        for i in nums:
            c |=i
        return c * (1 << (len(nums) - 1))
"""
from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        c=0
        n = len(nums)
        for i in range(1, n+1):
            for k in combinations(nums, i):
                x = 0
                for j in range(len(k)):
                    x ^= k[j]
                c += x
        return c
"""