class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s)==len(words):
            for i in range(len(words)):
                k=words[i]
                if k[0]!=s[i]:
                    return False
            return True
        return False