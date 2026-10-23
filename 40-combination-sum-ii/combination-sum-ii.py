class Solution:

    def sum2(self,l1,l2,target,nums,tsum,start):
        if target==tsum:
            l2.append(l1.copy())
            return

        if tsum>target:
            return

        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            l1.append(nums[i])
            self.sum2(l1,l2,target,nums,tsum+nums[i],i+1)

            l1.pop()

    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:

        l1 = []
        l2 = []
        tsum = 0
        nums.sort()
        self.sum2(l1,l2,target,nums,tsum,0)

        return l2
        