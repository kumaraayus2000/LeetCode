class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0

        for x1 in moves:
            if x1== "U":
                y=y+1
            elif x1=="D":
                y=y-1
            elif x1 =="L":
                x=x-1
            elif x1 =="R":
                x=x+1

        if x==0 and y==0:
            return True
        
        return False
            
