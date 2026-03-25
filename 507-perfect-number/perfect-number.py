class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s=1
        if num<=1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                s+=i+num//i
        return num==s