/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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

    TreeNode *inorder(vector<int>v1,int start,int end){
        if(start>end){
            return NULL;
        }

        int mid = (start+end) /2;
        TreeNode* root = new TreeNode(v1[mid]);
        root->left = inorder(v1,start,mid-1);
        root->right = inorder(v1,mid+1,end);

        return root;
    }
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int>v1;

        ListNode *tmp = head;
        while(tmp!=NULL){
            v1.push_back(tmp->val);
            tmp=tmp->next;
        }

        return inorder(v1,0,v1.size()-1);


    }
};