class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        s=""
        su=0
        t=n
        while n>0:
            k=n%10
            su+=k
            if k!=0:
                s+=str(k)
            n//=10
        s=int(s[::-1])
        if t>0:
            return s*su  
        else:
            return 0    


        