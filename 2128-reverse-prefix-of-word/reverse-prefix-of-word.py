class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c=len(word)
        if ch not in word:
            return(word)  
        for i in range(len(word)):
            if word[i]==ch:
                c=i
                break
        k=word[:c+1]
        s=k[::-1]
        k=s+word[c+1:]
        return k