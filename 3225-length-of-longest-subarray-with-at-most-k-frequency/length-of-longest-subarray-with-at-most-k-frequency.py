
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mp = {}

        j = 0
        max_len = 0

        for i in range(len(nums)):
            # Add current number into current window
            mp[nums[i]] = mp.get(nums[i], 0) + 1

            # If current number appears more than k times,
            # shrink window from the left
            while mp[nums[i]] > k:
                mp[nums[j]] -= 1
                j += 1

            # Update maximum valid window length
            max_len = max(max_len, i - j + 1)

        return max_len