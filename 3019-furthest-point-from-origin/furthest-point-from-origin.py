class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x,y=0,0
        x=moves.count('L')
        y=moves.count('R')
        u=moves.count('_')
        return abs(x-y)+u