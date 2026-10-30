class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        a=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i==j or j==k or i==k:
                        continue
                    num=digits[i]*100 + digits[j]*10 + digits[k]
                    if digits[i]!= 0 and digits[k] % 2 == 0:
                        a.add(num)
        return sorted(a)
