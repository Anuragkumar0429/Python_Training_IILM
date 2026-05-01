class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # 1. Split the list into two halves using slow/fast pointers
        mid = self.getMid(head)
        right_head = mid.next
        mid.next = None  # Sever the link to split the list
        
        # 2. Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(right_head)
        
        # 3. Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        # Use slow and fast pointers to find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Attach the remaining nodes
        tail.next = list1 if list1 else list2
        return dummy.next