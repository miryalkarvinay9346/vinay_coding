class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        b=[False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                b[i]=True
        return b