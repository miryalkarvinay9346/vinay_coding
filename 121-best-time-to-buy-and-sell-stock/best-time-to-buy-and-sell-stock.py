class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=float('inf')#infinite initial
        maxProfit=0#initial value
        for price in prices:
            if price<minPrice:
                minPrice=price
            profit=price-minPrice
            if profit>maxProfit:
                maxProfit=profit
        return maxProfit