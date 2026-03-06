class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        maxsum = nums[0]

        for i in range(1,len(nums)):
            sum = max(nums[i],sum+nums[i])
            maxsum = max(sum,maxsum)

        return maxsum