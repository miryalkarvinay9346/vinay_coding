class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        c=0
        for i in  range(n):
            current=self.check(s[i])
            if (i+1<n)and (current<self.check(s[i+1])):
                c-=current#Smaller number before larger number → subtract
            else:
                c+=current
        return c
    def check(self, ch: str) -> int:
        if ch=='I':
            return 1
        elif ch=='V':
            return 5
        elif ch=='X':
            return 10
        elif ch=='L':
            return 50
        elif ch=='C':
            return 100
        elif ch=='D':
            return 500
        elif ch=='M':
            return 1000
        else:
            return 0