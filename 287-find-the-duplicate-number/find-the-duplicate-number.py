class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        for num in nums:

            index = abs(num)

            # Already visited this number
            if nums[index] < 0:
                return index

            # Mark as visited
            nums[index] *= -1