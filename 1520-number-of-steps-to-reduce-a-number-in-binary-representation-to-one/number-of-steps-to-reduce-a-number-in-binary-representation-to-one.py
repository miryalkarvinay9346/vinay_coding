class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        a=int(s,2)
        if (a==1):
            return c
        else:
            while(a!=1):
                if(a%2==0):
                    a=a//2
                elif(a%2!=0):
                    a=a+1
                c=c+1
            return c   

        