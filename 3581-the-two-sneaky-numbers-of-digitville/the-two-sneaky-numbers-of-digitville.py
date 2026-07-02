class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        seen=set()
        for i in nums:
            if i in seen:
                a.append(i)
            else:
                seen.add(i)
        return a
        