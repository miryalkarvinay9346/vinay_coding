class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        i=False
        for ch in s:
            if ch=="|":
                i=not i
            elif ch=="*"  and not i:
                c+=1
        return c