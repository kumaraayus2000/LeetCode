class Solution:
    def maxProduct(self, n: int) -> int:
        
        l1 = []
        n1 = n
        while n1>0:
            n2= n1%10
            l1.append(n2)
            n1= n1//10

        l1.sort(reverse=True)

        return l1[0] * l1[1]