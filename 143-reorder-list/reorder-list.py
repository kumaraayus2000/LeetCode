# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        l1 = []

        tmp = head

        while tmp:
            l1.append(tmp.val)
            tmp = tmp.next

        i = 0
        j = len(l1)-1
        l2 = []
        while i < len(l1) and j>=0:
            l2.append(l1[i])
            i+=1
            l2.append(l1[j])
            j-=1


        tmp1 = head
        j=0
        while tmp1:
            tmp1.val = l2[j]
            tmp1 = tmp1.next
            j+=1

        return head
        