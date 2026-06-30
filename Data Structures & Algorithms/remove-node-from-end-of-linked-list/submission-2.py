# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        prev=None
        len=0
        while curr:
            len+=1
            curr=curr.next
        curr=head
        i=0
        if len==n:
            return curr.next
        for i in range (len):
            if (len-n)==i:
                prev.next=curr.next
                return head
            else:
                prev=curr
                curr=curr.next
                