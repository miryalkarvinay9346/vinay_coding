class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1=0
        res1=0
        c0=0
        res0=0
        for i in range(len(s)):
            if s[i]=="1":
                c1+=1
                c0=0
                res1=max(res1,c1)
            else:
                c0+=1
                c1=0
                res0=max(res0,c0)    
        return res1>res0        


        