class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        k=""
        for i in a:
            k=k+i[::-1]+" "
        return k[:len(k)-1]
        