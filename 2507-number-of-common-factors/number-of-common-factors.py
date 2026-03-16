class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c=0
        for i in range(1,min(a,b)+1): #we can also use max(a,b) but it take more time than min(a,b) , since common values are found before(<=) the min value
            if(a%i==0 and b%i==0):
                c+=1
        return c        
        