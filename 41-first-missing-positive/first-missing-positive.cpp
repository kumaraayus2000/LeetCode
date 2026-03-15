class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
        int n = nums.size();
        while (true) {
            bool changed = false;

            for (int i = 0; i < n; i++) {
                // current number should be in range [1, n]
                // and not already in correct place
                while (nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
                    swap(nums[i], nums[nums[i] - 1]);
                }
            }
            break;
        }

        // Find the first index where value is not index+1
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        // If all positions are correct, answer is n+1
        return n + 1;
    }
};