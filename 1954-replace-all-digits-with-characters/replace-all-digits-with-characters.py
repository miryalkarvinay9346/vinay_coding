class Solution:
    def replaceDigits(self, s: str) -> str:
        a=[]
        k=""
        """
        for i in range(1,len(s),2):
            p=int(s[i])
            b=s[i-1]
            a.append(self.shift(b,p))
        """
        for i in range(len(s)):
            if i%2==0:
                k+=s[i]
            else:
                p=int(s[i])
                b=s[i-1]
                k+=chr(ord(b)+p) #self.shift(b,p)
        return k
    """def shift(self,c:str,x:int)->str:
        return chr(ord(c)+x)"""

        