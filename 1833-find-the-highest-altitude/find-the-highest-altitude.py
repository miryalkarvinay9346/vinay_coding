class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0,gain[0]]
        for i in range(1,len(gain)):
            a.append(gain[i]+a[i])
        return max(a)
