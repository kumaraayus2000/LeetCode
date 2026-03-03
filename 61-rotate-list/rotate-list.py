# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k==0:
            return head

        tmp = head
        length =1
        while tmp.next is not None:
            tmp = tmp.next
            length +=1
        tail = tmp

        k%=length
        if k==0:
            return head

        new_tail = head
        for _ in range(length - k -1):
            new_tail = new_tail.next
        
        new_head = new_tail.next

        tail.next = head
        new_tail.next = None

        return new_head
        