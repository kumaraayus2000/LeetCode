class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

          int i = m - 1;           // last valid index in nums1
        int j = n - 1;           // last index in nums2
        int k = m + n - 1;       // fill position in nums1 (from the end)

        // Merge by placing the larger of nums1[i], nums2[j] at nums1[k]
        while (j >= 0) {         // while nums2 still has elements to place
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

    }
};