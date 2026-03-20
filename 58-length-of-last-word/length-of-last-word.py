class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        a=s[::-1]
        a=a.strip()
        c=0
        for i in range(0,len(a)):
            if(a[i]==" " and c>0):
                break
            else:
                c+=1    
        return c
        