class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        # initialize with any valid triplet sum
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                # update closest if this sum is closer to target
                if abs(s - target) < abs(closest - target):
                    closest = s

                # move pointers
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return s  # exact match

        return closest