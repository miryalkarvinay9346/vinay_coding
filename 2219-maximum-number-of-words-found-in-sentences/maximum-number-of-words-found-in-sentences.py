class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in sentences:
            if len(i.split())>m:
                m=len(i.split())
        return m