class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if len(s)==k:
            return s[::-1]
        return s[k-1::-1] + s[k:]
