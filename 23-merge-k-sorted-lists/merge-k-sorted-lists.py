# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self,list1:Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None:
        #     return list2

        # if list2 is None:
        #     return list1

        # if list1.val < list2.val:
        #     list1.next = self.merge(list1.next,list2)
        #     return list1
        # else:
        #     list2.next = self.merge(list1,list2.next)
        #     return list2
        
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1=list1.next
            else:
                tail.next = list2
                list2=list2.next

            tail=tail.next


        if list1 is None:
            tail.next = list2

        if list2 is None:
            tail.next = list1
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        ans = None

        for lis in lists:
            ans = self.merge(ans,lis)

        return ans
        