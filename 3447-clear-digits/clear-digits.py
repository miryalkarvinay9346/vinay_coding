class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
        """
        s = list(s)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                s.pop(i)      # remove digit
                s.pop(i - 1)  # remove character before it
                i -= 1
            else:
                i += 1
        return ''.join(s)
        """
