class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry =0
        res = []

        while i>=0 or j>=0 or carry:
            if i>=0:
                bita = int(a[i])
            else:
                bita = 0
            
            if j>=0:
                bitb = int(b[j])
            else:
                bitb = 0

            total = bita + bitb + carry

            res.append(str(total%2))

            carry = total//2

            i-=1
            j-=1

        return "".join(res[::-1])
        