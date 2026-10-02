class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=[]
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                a.append(s[i])
        res=[]
        i=0
        for ch in s:
            if ch.isalpha():
                res.append(a[i])
                i += 1
            else:
                res.append(ch)
        return ''.join(res)