class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=['[','{','(']
        r=[']','}',')']
        a=list(s)
        if(len(s)%2!=0):
            return False
        if s[0]==r[0] or s[0]==r[1] or s[0]==r[2]:
            return False
        i=0    
        while( i<len(a)-1):
            if (a[i] == '(' and a[i+1] == ')') or (a[i] == '{' and a[i+1] == '}') or (a[i] == '[' and a[i+1] == ']'):
                a.pop(i)
                a.pop(i)
                i=max(i-1,0)    
            else:
                i+=1
        return len(a)==0            


        