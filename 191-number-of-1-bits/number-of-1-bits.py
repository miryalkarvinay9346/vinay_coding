class Solution:
    def hammingWeight(self, n: int) -> int:
        c=str(bin(n))
        return c.count("1")
        