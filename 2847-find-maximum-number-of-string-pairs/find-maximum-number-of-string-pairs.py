class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                a=words[i]
                b=words[j]
                if a==b[::-1]:
                    c+=1
        return c