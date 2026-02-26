class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        cd=0
        an=num
        dc=len(str(abs(num)))
        for i in range(dc):
            rem=num%10
            if(an%rem==0):
                cd=cd+1
            num=num/10
        return cd        


        