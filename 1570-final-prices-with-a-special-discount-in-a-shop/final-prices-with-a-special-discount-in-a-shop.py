class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        a=[0]*len(prices)
        for i in range(len(prices)):
            k=prices[i]
            for j in range(i+1,len(prices)):
                if i<j and prices[i]>=prices[j]:
                    k-=prices[j]
                    break
            a[i]=k
        return a