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
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode * tmp = head;

        while(tmp!=NULL && tmp->next!=NULL){
            int v1 = tmp->val;
            tmp->val = tmp->next->val;
            tmp->next->val = v1;

            tmp=tmp->next->next;
        }
        return head;
    }
};