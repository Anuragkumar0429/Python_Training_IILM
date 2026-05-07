# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If there is only one node, deleting it returns None
        if not head or not head.next:
            return None
        
        # Initialize pointers
        # 'slow' will eventually point to the node BEFORE the middle
        # 'fast' starts two steps ahead to create the necessary offset
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow.next is the middle node; skip it to "delete" it
        slow.next = slow.next.next
        
        return head