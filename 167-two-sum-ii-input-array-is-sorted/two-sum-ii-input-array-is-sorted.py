class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        --- this causes TLE ERROR ,due to time complexity is O(n^2) ---
        a=[0,0]
        for i in range(len(numbers)):
            a[0]=i+1
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    a[1]=j+1
                    return a
            """
        l=0
        r=len(numbers)-1
        while l<r:
            total=numbers[l]+numbers[r]
            if total==target:
                return[l+1, r+1]
            elif total < target:#you need a larger sum → move left right.
                l+=1
            else:#you need a smaller sum → move right left.
                r-= 1