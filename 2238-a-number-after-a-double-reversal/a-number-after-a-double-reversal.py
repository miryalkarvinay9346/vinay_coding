class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """ 
        1) if num contains ending with zero and
            the double reversed digit is not equal to actual digit
        2) if it is zero , double revesed == actual digit
        """
        if num!=0 and num%10==0:
            return False
        return True        