class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<=2:
            return 0

        prime = [True] * n

        prime[0] = False
        prime[1] = False

        x = 2

        while x*x<n:

            if prime[x]:
                multiple = x*x

                while multiple < n:
                    prime[multiple] = False
                    multiple+=x

            x+=1

        return sum(prime)