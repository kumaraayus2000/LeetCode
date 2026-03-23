class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1

        l1 = []

        for i in range(len(nums)):
            if mp[nums[i]]>1:
                l1.append(nums[i])
                mp[nums[i]]=0
        
        return l1