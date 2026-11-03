from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:

        maximum = max(nums)
        sum1 =0
        for x1 in nums:
            sum1 = sum1 + maximum-x1

        return sum1