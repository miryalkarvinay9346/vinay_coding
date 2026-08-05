class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        #a=s.split()
        """
        b=""
        c=0
        for i in range(len(s)):
            if c>k-1:
                b=b+s[i]
                break
            else:
                b=b+s[i]
                if s[i]==" ":
                    c+=1
        print(str(b[:len(b)-2]))
        """
        s=s.split(" ")[:k]
        return " ".join(s)
        