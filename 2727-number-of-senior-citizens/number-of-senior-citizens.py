class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            if  int(i[-4:-2])>60:
                c+=1
        return c