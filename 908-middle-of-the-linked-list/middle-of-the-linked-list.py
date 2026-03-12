# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l1 = head
        l2 =head
        while l1 is not None and l1.next is not None:
            l1=l1.next.next
            l2=l2.next

        return l2
        