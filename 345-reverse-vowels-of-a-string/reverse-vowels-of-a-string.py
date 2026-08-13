class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        """
        a = []
        indexs = []
        for i in range(len(s)):
            if s[i] in vowels:
                a.append(s[i])
                indexs.append(i)
        p = []
        k = len(a) - 1
        for j in range(len(s)):
            if j in indexs:
                p.append(a[k])
                k -= 1
            else:
                p.append(s[j])
        return "".join(p)
        """
        a = []
        indexs = set()
        for i in range(len(s)):
            if s[i] in vowels:
                a.append(s[i])
                indexs.add(i)
        p = []
        k = len(a) - 1
        for j in range(len(s)):
            if j in indexs:
                p.append(a[k])
                k -= 1
            else:
                p.append(s[j])
        return "".join(p)
