# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        h = t = None
        temp = tm = None
        while head.next:
            if head.val == head.next.val or head.val == (temp and temp.val):
                temp = head
                head = head.next
            else:
                tm = temp = head
                head = head.next
                tm.next = None
                if h == None:
                    h = t = tm
                else:
                    t.next = tm
                    t = tm
        if head.val != (temp and temp.val):
            if h == None:
                h = t = head
            else:
                t.next = head
                t = head
        return h