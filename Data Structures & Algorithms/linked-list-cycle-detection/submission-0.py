# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        seen =set()
        while curr:
            if id(curr) in seen:
                return True
            else:
                seen.add(id(curr))
                curr=curr.next
        return False