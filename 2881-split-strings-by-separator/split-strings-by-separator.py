class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        a=[]
        for i in words:
            k=i.split(separator)
            for w in k:
                if w:
                    a.append(w)
        return a