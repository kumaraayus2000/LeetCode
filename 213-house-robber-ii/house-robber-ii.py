class Solution:

    def robsum(self,nums):
        if len(nums)==1:
            return nums[0]

        n1 = len(nums)
        dp = [0] * n1

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n1):
            dp[i] = max(dp[i-1],nums[i]+ dp[i-2])

        return dp[n1-1]


    def rob(self, nums: list[int]) -> int:
        
        if len(nums)==1:
            return nums[0]

        return max(self.robsum(nums[1:]),self.robsum(nums[:-1]))

