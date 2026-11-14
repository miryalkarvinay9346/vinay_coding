class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        a=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if words[i] in words[j]:
                        a.append(words[i])
                    elif words[j] in words[i]:
                        a.append(words[j])
        return list(set(a))