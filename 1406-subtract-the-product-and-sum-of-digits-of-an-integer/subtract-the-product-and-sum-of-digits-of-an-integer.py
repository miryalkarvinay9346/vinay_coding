class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #s=0
        #p=1
        #while n>0:
        #    s+=n%10
        #    p*=n%10
        #    n=n//10
        arr=list(map(int,str(n)))
        s=sum(arr)
        p=math.prod(arr)
        return p-s  
        