class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in range(0,len(digits)):
            s=s+str(digits[i])
        s=str(int(s)+1)
        a=[]
        for i in range(0,len(s)):
            a.append(int(s[i]))
        return a   

        