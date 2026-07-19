class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l1 = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            l1 = max(sum,l1)

            if sum<0:
                sum=0
            

        return l1
            
