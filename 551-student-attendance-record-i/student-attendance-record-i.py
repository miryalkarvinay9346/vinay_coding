class Solution:
    def checkRecord(self, s: str) -> bool:
        f=0
        l=0
        for i in range(0,len(s)):
            if s[i]=='A':
                f+=1
                if f>= 2:
                    return False
            if s[i]=="L":
                l+=1
                if l>= 3:
                    return False
            else:
                l=0
            
            
        return True