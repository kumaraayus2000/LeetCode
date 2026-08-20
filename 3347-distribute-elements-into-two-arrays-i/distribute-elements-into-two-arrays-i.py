class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        l1 = []
        l2 = []
        l1.append(nums[0])
        l2.append(nums[1])

        for i in range(2,len(nums)):
            if l1[len(l1)-1] > l2[len(l2)-1]:
                l1.append(nums[i])
            else:
                l2.append(nums[i])

        return l1 + l2