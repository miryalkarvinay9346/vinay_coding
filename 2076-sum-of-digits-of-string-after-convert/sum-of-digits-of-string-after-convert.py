class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=""
        for x in s:
            n+=str(ord(x)-96)
        a=int(n)    
        while(k>0):
            ans=0
            while(a>0):
                ans+=a%10
                a/=10
            a=ans    
            k-=1    
        return ans    
