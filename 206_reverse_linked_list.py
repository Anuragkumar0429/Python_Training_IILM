class Solution (object):
    def reverseList(self,head):
        p = None
        while head:
            t = head
            head = head.next
            t.next = p
            p=t
        return p