class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        s=2*(10**4)
        for i in range(len(tasks)):
            a=sum(tasks[i])
            if a<s:
                s=a
        return s
