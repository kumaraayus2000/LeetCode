from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        # Result initialized with 0
        result = [0] * n

        # Stack stores indices
        stack = []

        for i in range(n):

            # If current temperature is warmer than
            # the temperature at the top stack index
            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev_index = stack.pop()

                # Number of days waited
                result[prev_index] = i - prev_index

            # Current day now waits for a warmer day
            stack.append(i)

        return result