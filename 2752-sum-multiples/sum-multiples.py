class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s=0
        for i in range(1,n+1):
            if i%(3*5*7)==0:
                s+=i
            elif i%3==0:
                s+=i
            elif i%5==0:
                s+=i
            elif i%7==0:
                s+=i
        return s                 
        