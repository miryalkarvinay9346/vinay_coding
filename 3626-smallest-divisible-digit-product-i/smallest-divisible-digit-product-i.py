class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while 1:
            p=1
            num=n
            while num>0:
                p*=num%10
                num//=10
                if p==0:
                    break
            if  p%t==0:
                return n
            n+=1