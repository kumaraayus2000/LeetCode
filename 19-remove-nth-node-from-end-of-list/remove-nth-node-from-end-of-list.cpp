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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        if(head==NULL || head->next==NULL){
            return NULL;
        }

        ListNode *res = head;
        int l=0;
        while(res!=NULL){
            res=res->next;
            l++;
        }
        if(n==l){
            return head->next;
        }
        
        int l1 = l-n-1;
        ListNode *res1=head;
        for(int i=0;i<l1;i++){
            res1=res1->next;
        }
        res1->next=res1->next->next;
        return head;

    }
};