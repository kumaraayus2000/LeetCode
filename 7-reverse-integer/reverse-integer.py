class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign =-1
        else:
            sign = 1
        
        x = abs(x)
        res = 0

        while x>0:
            digit = x %10
            res = res *10 + digit
            x//=10

        res = sign * res
    
        if res < -2 ** 31 or res > 2 **31 -1:
            return 0
        
        return res
        