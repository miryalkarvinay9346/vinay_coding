class Solution:
    def sortSentence(self, s: str) -> str:
        k=s.split()
        a=[""]*len(k)
        for i in k:
            j=int(i[-1])
            a[j-1]=i[:len(i)-1]
        return " ".join(a)