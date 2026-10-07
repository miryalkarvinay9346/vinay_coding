class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        k=""
        for i in s:
            if i=="(":
                if c>0:
                    k+=i
                c+=1#increase count after 
            else:
                c=c-1#decrease before and chek if it is outer
                if c>0:
                    k+=i
        return k