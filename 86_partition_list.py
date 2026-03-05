# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return None
        h1 = t1 = h2 = t2 = None
        while head:
            temp = head
            head = head.next
            temp.next = None
            if temp.val < x:
                if h1 == None:
                    h1 = t1 = temp
                else:
                    t1.next = temp
                    t1 = temp
            else:
                if h2 == None:
                    h2 = t2 = temp
                else:
                    t2.next = temp
                    t2 = temp
        if h1 == None:
            return h2
        elif h2 == None:
            return h1

        t1.next = h2

        return h1