class Solution:
    # Helper function to convert a single Roman character to its integer value
    def value(self, x: str) -> int:
        if x == 'I': return 1
        if x == 'V': return 5
        if x == 'X': return 10
        if x == 'L': return 50
        if x == 'C': return 100
        if x == 'D': return 500
        if x == 'M': return 1000
        return 0  # safety fallback

    def romanToInt(self, s: str) -> int:
        total = 0  # stores final integer result

        # Loop through each character in the string
        for i in range(len(s)):
            curr = self.value(s[i])  # value of current Roman character

            # RULE:
            # If current value is smaller than the next value,
            # we subtract it (e.g., I before V → IV = 4)
            if i + 1 < len(s) and curr < self.value(s[i + 1]):
                total -= curr
            else:
                # Otherwise, we add it normally
                total += curr

        return total
