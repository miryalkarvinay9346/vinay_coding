class Solution:
    def totalMoney(self, n: int) -> int:

        if n<=7:
            return n*(n+1)//2
        s=0    
        for i in range(n):
            wn=i//7
            day_of_week=i%7
            s+=wn+1+day_of_week
        return s    


        