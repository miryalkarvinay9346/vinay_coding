class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        c=0
        n=len(strs)
        m=len(strs[0])
        for i in range(m):
            for j in range(1,n):
                if strs[j][i]<strs[j-1][i]:
                    c+=1
                    break
        return c