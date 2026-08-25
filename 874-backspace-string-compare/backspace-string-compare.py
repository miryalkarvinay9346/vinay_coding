class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            a=[]
            for ch in s:
                if ch == '#':
                    if a:
                        a.pop()
                else:
                    a.append(ch)
            return ''.join(a)
        return build(s) == build(t)
