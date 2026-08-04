class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        c=0
        for i in words:
            if all(ch in a for ch in i):
                c+=1
        return c