/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    TreeNode* createtree(vector<int>&nums,int start,int end)  {
        if(start>end){
            return NULL;
        }

        int mid = (start+end)/2;
        TreeNode* tmp = new TreeNode(nums[mid]);

        tmp->left = createtree(nums,start,mid-1);

        tmp->right = createtree(nums,mid+1,end);

        return tmp;

    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        
        int mid = nums.size()/2;

        int x = nums[mid];

        return createtree(nums,0,nums.size()-1);

    }
};