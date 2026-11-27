class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l1 = 0
        c1 = 0
        c2 = 0
        l2 =0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                l1+=1
            else:
                c1 = max(c1,l1)
                l1=0
        
        c1 = max(c1,l1)


        for i in range(len(nums)-1,0,-1):
            if nums[i]<nums[i-1]:
                l2+=1
            else:
                c2 = max(c2,l2)
                l2=0
        
        c2 = max(c2,l2)

        if c1 + c2 ==0:
            return 1

        return max(c1,c2)+1
            


        

        