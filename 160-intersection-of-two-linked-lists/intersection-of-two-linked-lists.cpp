/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int getlen(ListNode* headA){

        ListNode *a1 = headA;
        int l1=0;
        while(a1!=NULL){
            a1=a1->next;
            l1++;
        }
        return l1;
    }

    ListNode *compare(ListNode *a,ListNode *b){

        while(a!=b){
            a=a->next;
            b=b->next;
        }
        return a;
    }
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *a=headA;
        ListNode *b = headB;

        int l1 = getlen(headA);
        int l2 = getlen(headB);

        if(l1>l2){
            int n1 = l1-l2;
            for(int i=0;i<n1;i++){
            a=a->next;
            }
            return compare(a,b);
        }else{
            int n1 = l2-l1;
            for(int j=0;j<n1;j++){
                b=b->next;
            }
            return compare(a,b);

        }
        return NULL;

    }
};