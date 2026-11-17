class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sa,sb=0,0
        for i in nums:
            if i>=10:
                sa+=i
            else:
                sb+=i
        return sa!=sb