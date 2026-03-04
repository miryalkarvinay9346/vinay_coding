class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=""  #empty string
        for ch in s:
            if ch.isalnum():#check if it is character
                a+=ch.lower()#concate
        return a==a[::-1]#return if reverse istrue