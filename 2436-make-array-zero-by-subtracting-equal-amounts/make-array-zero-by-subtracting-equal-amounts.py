class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        a=[]
        for i in  nums:
            if i!=0 and i not in a:
                a.append(i)
        return len(a)
        """
        return len(set(nums) - {0})
        """
        