class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mp = {}

        for x in nums:
            if x in mp:
                return True        
            mp[x] = mp.get(x,0)+1

        return False

        