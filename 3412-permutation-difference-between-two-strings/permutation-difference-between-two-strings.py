class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a=0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    a+=abs(i - j)
        return a