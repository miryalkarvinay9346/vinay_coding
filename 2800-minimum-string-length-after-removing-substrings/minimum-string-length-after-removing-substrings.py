class Solution:
    def minLength(self, s: str) -> int:
        """
        a=[]
        for i in s:
            if a:
                if (a[-1]=="A" and i=="B"):
                    a.pop()
                elif (a[-1]=='C' and i=='D'):
                    a.pop()
                else:
                    a.append(i)
            else:
                a.append(i)
        return len(a)
        """
        while "AB" in s or "CD" in s:
            s=s.replace("AB","").replace("CD","")
        return len(s)
        