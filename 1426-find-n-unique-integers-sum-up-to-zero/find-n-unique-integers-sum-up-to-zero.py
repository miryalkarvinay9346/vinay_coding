class Solution:
    def sumZero(self, n: int) -> List[int]:
        a=[0]*n
        c=1
        for i in range(n//2):
            a[i]=c
            a[n-(i+1)]=-c
            c+=1
        return a


        