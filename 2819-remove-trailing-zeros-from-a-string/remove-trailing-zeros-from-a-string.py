class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        k=num[::-1]
        k=str(int(k))[::-1]
        return k