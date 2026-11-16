class Solution:

    def modify(self, s1):
        total = 0

        for x in s1:
            total += int(x)

        return str(total)


    def digitSum(self, s: str, k: int) -> str:

        s2 = s

        while len(s2) > k:

            new_string = ""

            # Take groups of k characters
            for i in range(0, len(s2), k):

                # Get current group
                s1 = s2[i:i+k]

                # Find digit sum of current group
                s1 = self.modify(s1)

                # Add result to new string
                new_string += s1

            # New string becomes our input
            s2 = new_string

        return s2