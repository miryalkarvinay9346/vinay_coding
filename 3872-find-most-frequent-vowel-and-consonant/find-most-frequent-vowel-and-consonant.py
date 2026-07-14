import math
class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        a="aeiou"
        mc=[0]
        c=max(s.count('a'),s.count('e'),s.count('i'),s.count('o'),s.count('u'))
        for i in range(len(s)):
            if s[i] not in a:
                mc.append(s.count(s[i]))
        k=max(mc)                
        return c+k