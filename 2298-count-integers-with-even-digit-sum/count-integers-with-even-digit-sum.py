class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            s=0
            while i>0:
                s+=i%10
                i=i//10
            if s%2==0:
                c+=1
        return c