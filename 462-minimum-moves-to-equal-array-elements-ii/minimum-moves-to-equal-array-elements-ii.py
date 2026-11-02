class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()

        median = nums[len(nums)//2]

        x1 = 0
        for x in nums:
            x1 = x1+ abs(median-x)

        return x1