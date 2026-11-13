class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            if i*k not in nums:
                return i*k
            i=i+1
